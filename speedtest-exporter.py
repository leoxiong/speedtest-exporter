import json
import subprocess

from bottle import route, run, response


@route('/metrics')
def metrics():
    process = subprocess.run(['/usr/bin/speedtest', '--secure', '--json'], capture_output=True)
    result = json.loads(process.stdout)

    response.content_type = 'text/plain'
    return f'''# TYPE speedtest_rx_bytes_per_second gauge
speedtest_rx_bits_per_second{{host="{result["server"]["host"]}"}} {result["download"]}
# TYPE speedtest_tx_bytes_per_second gauge
speedtest_tx_bits_per_second{{host="{result["server"]["host"]}"}} {result["upload"]}'''


run(host='0.0.0.0', port=8080)
