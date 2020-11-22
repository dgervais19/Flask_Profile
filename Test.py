from flask import Flask, jsonify, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello! This is the home page"

@app.route("/profile/")
def profile():
    return render_template("profile.html")

@app.route("/login/")
def login():
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)