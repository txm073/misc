from flask import Flask, render_template_string
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template_string(open(os.path.join(os.path.dirname(__file__), "index.html"), "r").read())

if __name__ == "__main__":
    app.run(debug=True, port=8000)