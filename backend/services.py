from repository import Joke, JokeRepository

class JokeService:
    def __init__(self, repository: JokeRepository):
        self.repository = repository