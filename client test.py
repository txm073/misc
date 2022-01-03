from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify(message="Hello World!", response_type="JSON")

app.run(debug=True)