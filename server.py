import json
from time import time

from flask import Flask, request, jsonify, render_template, make_response
from flask_cors import CORS

from eyetracking import subscribe_eyetracking
from gaze_data_callback import set_extra_dirname_saved_csv
from exec_clang import exec_clang as _exec_clang
from storage_layout import storage_layout as _storage_layout
from storage_code import storage_code as _storage_code
from get_c_asset import get_program_file_name_from_order
from get_c_program import get_c_program
from get_c_question import get_c_question

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
        username = payload.get("username")
        order_of_program = payload.get("order_of_program")
        result = _exec_clang(code)
        print(result)
        _storage_code(code=code, username=username,
                     order_of_program=order_of_program, timestamp=str(time()))
        return jsonify({"result": result})

@app.route("/api/storage_layout", methods=['POST'])
def storage_layout():
    if request.method == "POST":
        payload = request.json
        layout = payload.get("layout")
        username = payload.get("username")
        _storage_layout(layout=layout, _path=username)
        return jsonify({ "result": "success" })

@app.route("/api/get_quiz", methods=["POST"])
def get_quiz():
    if request.method == "POST":
        payload = request.json
        order_of_quiz = payload.get("order_of_quiz")
        c_program = get_c_program(order_of_assets=order_of_quiz)
        c_question = get_c_question(order_of_assets=order_of_quiz)
        program_file_name = get_program_file_name_from_order(order_of_asset=order_of_quiz)
        set_extra_dirname_saved_csv(dirname=program_file_name)
        return jsonify({ "program": c_program, "question": c_question })
    
@app.route("/api/storage_code", methods=['POST'])
def storage_code():
    if request.method == "POST":
        try:
            payload = request.json
            code = payload.get("code")
            username = payload.get("username")
            order_of_program = payload.get("order_of_program")
            _storage_code(code=code, username=username,
                        order_of_program=order_of_program, timestamp=str(time()))
            return jsonify({ "status": "success" })
        except:
            return jsonify({ "status": "failure" })
 

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run()
