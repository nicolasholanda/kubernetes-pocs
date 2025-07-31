from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "App 1 - Frontend Service"

@app.route("/api")
def api():
    return "App 1 API Endpoint"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000) 