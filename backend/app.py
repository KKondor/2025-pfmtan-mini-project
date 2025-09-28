from flask import Flask
from services import JokeService

app = Flask(__name__)

joke_service = JokeService()

@app.route('/joke', methods=['GET'])
def get_joke():
    pass

@app.route('/leaderboard', methods=['GET'])
def get_leaderboard():
    pass

@app.route('/joke/<int:id>/rate', methods=['POST'])
def rate_joke(id):
    pass