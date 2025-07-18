from flask import Flask
import os

app = Flask(__name__)

greeting = os.environ.get("GREETING", "Hello")
secret_word = os.environ.get("SECRET_WORD", "(no secret)")

@app.route("/")
def hello():
    return f"{greeting} from Kubernetes! Secret word: {secret_word}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000) 