FROM python:3.9-alpine

RUN apk add --no-cache speedtest-cli && \
    pip install bottle

COPY speedtest-exporter.py .
RUN chmod +x ./speedtest-exporter.py

ENTRYPOINT ["python"]
CMD ["speedtest-exporter.py"]
