from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home/")
def get_homepage():
    return render_template("homepage.html")