from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def index():
    return "RBAC Demo App - Accessible by all authenticated users"

@app.route("/admin")
def admin():
    return "Admin Area - Requires admin permissions"

@app.route("/readonly")
def readonly():
    return "Read-Only Area - Requires read permissions"

@app.route("/namespace-info")
def namespace_info():
    namespace = os.environ.get('NAMESPACE', 'default')
    return f"Current namespace: {namespace}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000) 