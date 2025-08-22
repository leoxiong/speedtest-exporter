# `dirigera-exporter`

Prometheus speedtest metrics exporter.

1Build container image.

```bash
$ docker build -t registry.leoxiong.com/speedtest-exporter .
```

2Run image..

```yaml
services:
  ...
  speedtest-exporter:
    image: registry.leoxiong.com/speedtest-exporter
    expose:
      - 8080
    restart: unless-stopped
```

3Add Prometheus scrape config.

```yaml
scrape_configs:
  ...
  - job_name: speedtest-exporter
    metrics_path: /metrics
    scrape_interval: 30m
    scrape_timeout: 2m
    static_configs:
      - targets:
        - speedtest-exporter:8080
```
