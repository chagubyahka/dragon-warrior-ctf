from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/logins")
def logins():
    return render_template("logins.html")

@app.route("/robots.txt")
def robots():
    return send_from_directory(".", "robots.txt")

if __name__ == "__main__":
    app.run(debug=True)