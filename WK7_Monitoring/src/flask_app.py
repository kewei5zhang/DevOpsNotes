from flask import Flask, Response, request
import random
import time
from prometheus_flask_exporter import PrometheusMetrics
from app_helper import setup_metrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)
# Initialize any custom metrics (if needed)
setup_metrics(app)

# Example of static information as metric
metrics.info("app_info", "Application info", version="1.0.3")


@app.route("/")
def hello_world():
    return "👀 Monitoring Everyting!"


@app.route("/green")
def green():
    return "Green"


@app.route("/red")
def red():
    1 / 0  # This will cause a division by zero error
    return "Red"


ERROR_RATE = 0.1  # 10% chance of error
LATENCY_MIN = 100  # Minimum latency in milliseconds
LATENCY_MAX = 1000  # Maximum latency in milliseconds


@app.route("/simulation")
def simulation():
    # Simulate variable response latency
    latency_ms = random.uniform(LATENCY_MIN, LATENCY_MAX)
    time.sleep(latency_ms / 1000.0)

    if random.random() < ERROR_RATE:
        # Simulate an error
        raise Exception("Simulated error based on configured error rate.")

    return f"Request successful. Simulated latency: {latency_ms:.2f} milliseconds."


@app.errorhandler(500)
def handle_500(error):
    return str(error), 500


if __name__ == "__main__":
    app.run(debug=True)
