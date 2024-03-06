from flask import Flask, request, Response
from opentelemetry import metrics
from opentelemetry.exporter.prometheus import PrometheusMetricReader
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export.controller import PushController
import time
import sys

# Service name is required for most backends
resource = Resource(attributes={
    SERVICE_NAME: "your-service-name"
})

# Start Prometheus client
start_http_server(port=9464, addr="localhost")

# Set the MeterProvider and get a meter
reader = PrometheusMetricReader()
provider = MeterProvider(resource=resource, metric_readers=[reader])
metrics.set_meter_provider(provider)
meter = metrics.get_meter(__name__)

request_counter = meter.create_counter(
    name="request_count",
    description="Custom App Request Count",
    unit="1",
    value_type=int,
    label_keys=("service", "method", "endpoint", "status", "client"),
)

request_latency = meter.create_histogram(
    name="request_latency_seconds",
    description="Custom Request latency",
    unit="s",
    value_type=float,
    label_keys=("service", "method", "endpoint", "status", "client"),
)

def start_timer():
    request.start_time = time.time()

def stop_timer(response):
    resp_time = time.time() - request.start_time

    sys.stderr.write("Response time: %ss\n" % resp_time)

    request_latency.record(resp_time, {
        "service": "webapp",
        "method": request.method,
        "endpoint": request.path,
        "status": str(response.status_code),
        "client": "prometheus"
    })

    return response

def record_request_data(response):

    request_counter.add(
        1,
        {
            "service": "webapp",
            "method": request.method,
            "endpoint": request.path,
            "status": response.status_code,
            "client": "prometheus"
        }
    )

    return response

def setup_metrics(app):
    app.before_request(start_timer)
    app.after_request(record_request_data)
    app.after_request(stop_timer)

    # Function to expose metrics
    @app.route("/metrics")
    def metrics():
        return Response(prometheus_exporter.collect(), mimetype="text/plain")

    # Use the PushController to start the exporter
    controller = PushController(meter, prometheus_exporter, 5)
