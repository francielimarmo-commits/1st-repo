import os
from datetime import datetime
from flask import Flask, render_template

app = Flask(__name__, static_folder="static")

APP_NAME = os.getenv("APP_NAME", "1st-repo Docker Demo")
APP_VERSION = os.getenv("APP_VERSION", "0.1.0")
IMAGE_FILE = os.getenv("IMAGE_FILE", "pinguim.jpeg")
@app.get("/")
def home():
    return render_template(
        "index.html",
        app_name=APP_NAME,
        app_version=APP_VERSION,
        image_file=IMAGE_FILE,
    )

@app.get("/health")
def health():
    return {
        "status": "ok",
        "checked_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }


@app.get("/version")
def version():
    return {
        "app_name": APP_NAME,
        "version": APP_VERSION,
        "image_file": IMAGE_FILE
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
