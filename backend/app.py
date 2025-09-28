from flask import Flask, jsonify
from services import JokeService

app = Flask(__name__)

service = JokeService()

@app.route('/joke', methods=['GET'])
def get_joke():
    joke = service.generate_joke()
    return jsonify({"id": joke.id, "text": joke.text, "rating": joke.rating})

@app.route('/leaderboard', methods=['GET'])
def get_leaderboard():
    jokes = service.get_leaderboard()
    return jsonify([{"id": joke.id, 
                     "text": joke.text, 
                     "rating": joke.rating} for joke in jokes])

@app.route('/joke/<int:id>/rate', methods=['POST'])
def rate_joke(id):
    pass