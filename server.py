from flask import Flask, request, jsonify
from queue_manager import add_task

app = Flask(__name__)

@app.route("/login", methods=["POST"])
def login():

    data = request.json

    login = data["login"]
    password = data["password"]

    add_task(login,password)

    return jsonify({
        "status":"queued"
    })

app.run(host="0.0.0.0", port=5000)