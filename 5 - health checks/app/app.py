from flask import Flask, Response
import os

app = Flask(__name__)

@app.route("/")
def index():
    return "OK"

@app.route("/healthz")
def healthz():
    return "Healthy", 200

@app.route("/ready")
def ready():
    if os.path.exists("/tmp/ready"):
        return "Ready", 200
    else:
        return "Not Ready", 503

@app.route("/make-ready")
def make_ready():
    with open("/tmp/ready", "w") as f:
        f.write("ready")
    return "Marked ready"

@app.route("/make-unready")
def make_unready():
    if os.path.exists("/tmp/ready"):
        os.remove("/tmp/ready")
    return "Marked unready"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000) 