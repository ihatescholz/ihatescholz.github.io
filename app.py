from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search")
def username():
    Search = request.args.get("search")
    return render_template("search.html",search=Search)