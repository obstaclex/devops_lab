from flask import Flask, render_template, request
from handlers.pulls import get_pulls


app = Flask(__name__)


@app.route('/')
def index():
    return "Hello wrom Ilya Melnik"


@app.route('/pulls')
def pulls():
    state = request.args.get("state")
    return render_template("pulls.j2", pulls=get_pulls(state))


if __name__ == "__main__":
    app.run()
