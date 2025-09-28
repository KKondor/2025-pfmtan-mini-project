from flask import Flask
from repository import JokeRepository
from services import JokeService
from controller import FlaskController

def create_app():
    app = Flask(__name__)

    # repository és service példányosítása
    repo = JokeRepository()
    service = JokeService(repo)

    # controller inicializálása
    FlaskController(app, service)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
