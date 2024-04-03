from flask import Flask, Response, request
import random
import time
from prometheus_flask_exporter import PrometheusMetrics
from app_helper import setup_metrics
from my_logger import get_logger

# Create a Flask app
app = Flask(__name__)
log = get_logger(__name__)

# Use PrometheusMetrics to instrument the app
metrics = PrometheusMetrics(app)
metrics.info("app_info", "Application info", version="1.0.3")

# Use customized app_helper to instrument the app
setup_metrics(app)

@app.route("/")
def hello_world():
    log.info('Hello World')
    return "👀 Monitoring Everyting!"


@app.route("/green")
def green():
    log.info('hitting /green/ endpoint')
    return "Green"


@app.route("/red")
def red():
    log.info('hitting /red/ endpoint')
    try:
        1/0
    except Exception as e:
        log.exception(e)
        raise
    return 'red'


ERROR_RATE = 0.1  # 10% chance of error
LATENCY_MIN = 100  # Minimum latency in milliseconds
LATENCY_MAX = 1000  # Maximum latency in milliseconds


@app.route("/simulation")
def simulation():
    # Simulate variable response latency
    log.info('hitting /simulation/ endpoint')
    latency_ms = random.uniform(LATENCY_MIN, LATENCY_MAX)
    time.sleep(latency_ms / 1000.0)

    if random.random() < ERROR_RATE:
        # Simulate an error
        error_message = "Simulated error based on configured error rate."
        log.error(error_message)
        raise Exception(error_message)

    return f"Request successful. Simulated latency: {latency_ms:.2f} milliseconds."


@app.errorhandler(500)
def handle_500(error):
    log.error(f'something went wrong {error}')
    return str(error), 500


@app.errorhandler(404)
def handle_404(error):
    log.error(f'404 page not found {error}')
    return str(error), 404

if __name__ == "__main__":
    app.run(port=3001)
