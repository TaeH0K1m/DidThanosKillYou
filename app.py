from flask import Flask
from flask import render_template

import random

app = Flask(__name__)

@app.route('/')
def hello_world():
    isKilled = random.random()

    if isKilled < 0.5:
        return render_template("killed.html")
    else:
        return render_template("saved.html")

if __name__ == "__main__":
    app.run(debug=True)
