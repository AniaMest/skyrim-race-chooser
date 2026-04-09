from flask import Flask, render_template
import json

with open("survey.json") as f:
    survey = json.load(f)

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/race/<name>")
def race(name):
    return f"{name}"

@app.route("/quiz")
def quiz():
    return render_template("quiz.html", questions=survey["questions"])

if __name__ == "__main__":
    app.run(debug=True)