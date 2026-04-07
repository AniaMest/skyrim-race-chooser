from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/race/<name>")
def race(name):
    return f"{name}"

if __name__ == "__main__":
    app.run(debug=True)