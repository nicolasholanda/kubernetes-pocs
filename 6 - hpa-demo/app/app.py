from flask import Flask
import time
import os

app = Flask(__name__)

@app.route("/")
def index():
    return "HPA Demo App Running"

@app.route("/cpu")
def cpu_load():
    # Waits for 1 second
    start = time.time()
    while time.time() - start < 1:
        pass
    return "CPU load generated"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000) 