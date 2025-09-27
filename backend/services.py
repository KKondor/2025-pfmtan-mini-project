from repository import Joke, JokeRepository
import random

class JokeService:
    def __init__(self, repository: JokeRepository):
        self.repository = repository

    def generate_joke(self) -> Joke:
        random_id = random.randint(1, 600)
        joke = self.repository.get_joke_by_id(random_id)
        if joke:
            return joke
        else:
            raise ValueError("No joke found with the generated ID.")