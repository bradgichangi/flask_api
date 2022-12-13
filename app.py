from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug import exceptions

app = Flask(__name__)

@app.route('/')
def default():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=True)