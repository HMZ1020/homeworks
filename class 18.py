from flask import Flask

app = Flask(__name__)

@app.route("/")

def home():
    return "\n The best car is the 1999 Maxima☠🔥"

app.run(debug = True)