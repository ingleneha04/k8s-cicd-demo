
from flask import Flask, jsonify, request
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
import time

app = Flask(__name__)

REQUEST_COUNT = Counter(
    "app_http_requests_total",
    "Total HTTP requests",
    ["method", "endpoint", "http_status"]
)

REQUEST_LATENCY = Histogram(
    "app_http_request_duration_seconds",
    "HTTP request duration in seconds",
    ["endpoint"]
)


@app.before_request
def start_timer():
    request.start_time = time.time()


@app.after_request
def record_metrics(response):
    duration = time.time() - request.start_time

    REQUEST_COUNT.labels(
        request.method,
        request.path,
        str(response.status_code)
    ).inc()

    REQUEST_LATENCY.labels(request.path).observe(duration)
    return response


@app.route("/")
def home():
    return jsonify({
        "message": "Kubernetes CI/CD Demo Application",
        "status": "Running",
        "version": "1.0.0"
    })


@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200


@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {
        "Content-Type": CONTENT_TYPE_LATEST
    }
@app.route("/test-error")
def test_error():
    return jsonify({"status": "error", "message": "Grafana alert test"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
