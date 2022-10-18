from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    print(request.form["Message"])
    filepath = os.path.join(os.getcwd(), "logonclient.exe")
    os.spawnl(os.P_NOWAIT, filepath, "arg")
    return jsonify({"success": True})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)