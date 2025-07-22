from flask import Flask
import os
from datetime import datetime

app = Flask(__name__)
DATA_FILE = "/data/persist.txt"

@app.route("/")
def index():
    now = datetime.now().isoformat()
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, "a") as f:
        f.write(f"{now}\n")
    with open(DATA_FILE, "r") as f:
        content = f.read()
    return f"<pre>{content}</pre>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000) 