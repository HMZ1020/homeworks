from flask import Flask, render_template

app = flask(__name__)

@app.route("/")
def index():
    return render_template("endex.html")

app.run(debug = True)