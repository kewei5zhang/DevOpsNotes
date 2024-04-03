from flask import request
from datadog import DogStatsd
from prometheus_client import Counter, Histogram, Summary
import time
import sys

# Define metrics using prometheus_client
REQUEST_COUNT = Counter(
    "request_count",
    "Custom App Request Count",
    ["service", "method", "endpoint", "status", "client"],
)

REQUEST_LATENCY = Histogram(
    "request_latency_seconds",
    "Custom Request latency",
    ["service", "method", "endpoint", "status", "client"],
)

# Define metrics using datadog statsd
statsd = DogStatsd(host="statsd", port=9125)
REQUEST_COUNT_METRIC_NAME = "request_count_total"
REQUEST_LATENCY_METRIC_NAME = "request_latency_seconds_hist"

def start_timer():
    request.start_time = time.time()

def stop_timer(response):
    resp_time = time.time() - request.start_time

    # Application instrument using prometheus_client
    sys.stderr.write("Response time: %ss\n" % resp_time)
    REQUEST_LATENCY.labels(
        "webapp", request.path, request.path, response.status_code, "prometheus"
    ).observe(resp_time)

    # Application instrument using datadog statsd
    statsd.histogram(
        REQUEST_LATENCY_METRIC_NAME,
        resp_time,
        tags=[
            "service:webapp",
            "method:%s" % request.method,
            "endpoint:%s" % request.path,
            "status:%s" % str(response.status_code),
            "client:statsd"
        ],
    )
    return response

def record_request_data(response):

    # Application instrument using prometheus_client
    REQUEST_COUNT.labels(
        "webapp", request.method, request.path, response.status_code, "prometheus"
    ).inc()

    # Application instrument using datadog statsd
    statsd.increment(
        REQUEST_COUNT_METRIC_NAME,
        tags=[
            "service:webapp",
            "method:%s" % request.method,
            "endpoint:%s" % request.path,
            "status:%s" % str(response.status_code),
            "client:statsd"
        ],
    )
    return response

def setup_metrics(app):
    app.before_request(start_timer)
    # The order here matters since we want stop_timer
    # to be executed first
    app.after_request(record_request_data)
    app.after_request(stop_timer)
