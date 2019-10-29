import json

from flask import Flask, request, jsonify

from eyetracking import subscribe_eyetracking

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello World!"

unsubscriber_of_eyetracking = None
@app.route('/eyetracking', methods=['PUT'])
def eyetracking():
    if request.method == "PUT":
        global unsubscriber_of_eyetracking
        payload = request.json
        status = payload.get("status")
        if status == "start":
            unsubscriber_of_eyetracking = subscribe_eyetracking()
            return jsonify({ "status": "start" })
        elif status == "end":
            if unsubscriber_of_eyetracking != None:
                unsubscriber_of_eyetracking()
                return jsonify({ "status": "end" })
            else:
                return jsonify({ "status": "have not started yet" })

if __name__ == '__main__':
    app.run()
    
