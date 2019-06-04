import json
from flask import Flask
# from redis import Redis

import function.hello as hello

app = Flask(__name__)
# redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
    response = hello.handler()
    return json.dumps(response)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)