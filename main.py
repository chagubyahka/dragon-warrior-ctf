import os
from dotenv import load_dotenv
from flask import Flask, render_template, send_from_directory, request, redirect, url_for

load_dotenv()

app = Flask(__name__, template_folder='.')

USERNAME = os.getenv("DRAGON_USERNAME")
PASSWORD = os.getenv("DRAGON_PASSWORD")


@app.route("/")
def home():
    error = request.args.get("error")
    return render_template("index.html", error=error)


@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username", "").strip().lower()
    password = request.form.get("password", "").strip()

    if username == USERNAME and password == PASSWORD:
        return redirect(url_for("success")) 

    return redirect(url_for("home", error="Access denied"))


@app.route("/success")
def success():
    return render_template("success.html")


@app.route("/logins")
def logins():
    return render_template("logins.html")


@app.route("/robots.txt")
def robots():
    return send_from_directory(".", "robots.txt")

@app.route("/download")
def download_page():
    return render_template("download.html")

@app.route("/download-image")
def download_image():
    return send_from_directory(".", "secret.png", as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)