from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    if "name" in request.args:
        name = request.args["name"]
    else:
        name = "world"
    html = render_template("index.html", placeholder=name)
    return html

@app.route("/greet", methods=["GET", "POST"])
def greet():
    name = request.args.get("name", "world")
    return render_template("greet.html", name = name)