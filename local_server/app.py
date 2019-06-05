import json
from flask import Flask, jsonify

# Import your lambda function handlers here
from functions.hello import handler as hello

app = Flask(__name__)


@app.route('/')
def _hello():
    test_event = {
    }

    test_context = {

    }

    response = hello.hello(test_event, test_context)
    return jsonify(response)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)