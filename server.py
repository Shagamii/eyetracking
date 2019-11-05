import json

from flask import Flask, request, jsonify, render_template, make_response
from flask_cors import CORS

from eyetracking import subscribe_eyetracking
from exec_clang import exec_clang

app = Flask(__name__, static_folder="./dist/assets", template_folder="./dist")
CORS(app)

@app.route("/")
def index():
    return render_template("index.html")

unsubscriber_of_eyetracking = None
tracking_username = None
@app.route('/api/eyetracking', methods=['PUT'])
def eyetracking():
    if request.method == "PUT":
        global unsubscriber_of_eyetracking, tracking_username
        payload = request.json
        status = payload.get("status")
        username = payload.get("username") if payload.get(
            "username") != None else "default"
        if status == "start":
            if username == tracking_username:
                return make_response(jsonify({'error': 'Can not track eye with multiple people'}), 500)
            tracking_username = username
            unsubscriber_of_eyetracking = subscribe_eyetracking(username)
            return jsonify({"status": "start"})
        elif status == "end":
            if unsubscriber_of_eyetracking != None:
                unsubscriber_of_eyetracking()
                tracking_username = None
                return jsonify({"status": "end"})
            else:
                return jsonify({"status": "have not started yet"})


@app.route('/api/exec_clang', methods=['POST'])
def exec_clang():
    if request.method == "POST":
        payload = request.json
        code = payload.get("code")
        result = exec_clang(code)
        return jsonify({"result": result})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run()
