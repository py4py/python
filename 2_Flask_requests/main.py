# before starting install flask - pip install flask

from flask import Flask, request, jsonify, render_template

app = Flask(__name__)


users = [
        {
            "name": "John",
            "login": "john33",
            "password": "plainttext"
        },
        {
            "name": "Bob",
            "login": "bobNongrata63",
            "password": "plainttextPassword22"
        }
    ]


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html', my_users = users)


@app.route('/get_users', methods=['POST'])
def get_users():
    return jsonify({ "users" : users })


if __name__ == '__main__':
    app.run(debug=True)