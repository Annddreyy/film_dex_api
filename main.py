from flask import Flask, jsonify

from db import get_connection
from get_films import get_films_blueprint

app = Flask(__name__)

app.register_blueprint(get_films_blueprint)


if __name__ == '__main__':
    app.run(debug=True, port=1234)
