from flask import Flask, render_template, send_from_directory
import json, os

app = Flask(__name__)

def load_data():
    with open("data.json", "r", encoding="utf-8") as f:
        return json.load(f)

@app.route("/")
def index():
    data = load_data()
    return render_template("index.html", title=data.get("title", ""), people=data.get("people", []))

@app.route("/favicon.ico")
def favicon():
    if os.path.exists("static/favicon.ico"):
        return send_from_directory("static", "favicon.ico")
    return ("", 204)

if __name__ == "__main__":
    app.run(debug=True)
