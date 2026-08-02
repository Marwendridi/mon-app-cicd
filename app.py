import os
from flask import Flask

app = Flask(__name__)

VERSION = os.environ.get("APP_VERSION", "dev")

@app.route("/")
def home():
    return f"<h1>Pipeline Nightmare - Version 1</h1>"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

