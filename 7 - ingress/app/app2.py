from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "App 2 - Backend Service"

@app.route("/data")
def data():
    return "App 2 Data Endpoint"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000) 