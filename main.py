import os
from dotenv import load_dotenv
from flask import Flask, render_template, send_from_directory, request, redirect, url_for, session

load_dotenv()

app = Flask(__name__, template_folder='.')

app.secret_key = os.getenv("SECRET_KEY")
if not app.secret_key:
    raise ValueError("SECRET_KEY is not set")

USERNAME = os.getenv("DRAGON_USERNAME", "").strip().lower()
PASSWORD = os.getenv("DRAGON_PASSWORD", "")


@app.route("/")
def home():
    error = request.args.get("error")
    return render_template("index.html", error=error)


@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username", "").strip().lower()
    password = request.form.get("password", "").strip()

    if username == USERNAME and password == PASSWORD:
        session["logged_in"] = True
        return redirect(url_for("success"))

    return redirect(url_for("home", error="Access denied"))


@app.route("/success")
def success():
    if not session.get("logged_in"):
        return redirect(url_for("home", error="Login required"))
    return render_template("success.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("home"))


@app.route("/logins")
def logins():
    if not session.get("logged_in"):
        return redirect(url_for("home", error="Login required"))
    return render_template("logins.html")


@app.route("/robots.txt")
def robots():
    return send_from_directory(".", "robots.txt")


@app.route("/download")
def download_page():
    if not session.get("logged_in"):
        return redirect(url_for("home", error="Login required"))
    return render_template("download.html")


@app.route("/download-image")
def download_image():
    if not session.get("logged_in"):
        return redirect(url_for("home", error="Login required"))

    return send_from_directory(
        "static/img",
        "Kung-Fu-Panda.jpg",
        as_attachment=True,
        download_name="dragon-scroll.jpg"
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)