from flask import Flask, jsonify

from get_films import get_films_blueprint
from get_genres import get_genres_blueprint

app = Flask(__name__)

app.register_blueprint(get_films_blueprint)
app.register_blueprint(get_genres_blueprint)


if __name__ == '__main__':
    app.run(debug=True, port=1234)
