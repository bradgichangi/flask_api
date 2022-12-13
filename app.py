from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug import exceptions
import json


app = Flask(__name__)
CORS(app)

f = open('data.json')
data = json.load(f)

@app.route('/')
def default():
    return 'Welcome to the God of War API!'

@app.route('/characters')
def show_characters():
    return data['characters'], 200

@app.route('/character', methods = ['GET', 'POST'])
def create_character():
    if request.method == 'POST':
        sent_data = request.json
        arr = []
        data["characters"].append(sent_data['name'])
        # arr.append(sent_data['name'])
        with open("data.json", "w") as jsonFile:
            json.dump(data, jsonFile)
        return f"You have created a cat! It's called {sent_data['name']}", 201


if __name__ == '__main__':
    app.run(debug=True)