from repository import Joke, JokeRepository
from typing import Optional, List
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
        
    def get_leaderboard(self, sort_order: str = "desc", filter_type: str = "all") -> list[Joke]:
        return self.repository.get_jokes_list(sort_order, filter_type)
    
    def rate_joke(self, joke_id: int, value: int):
        if value != 1 and value != -1:
            raise ValueError("Value must be 1 (like) or -1 (dislike).")
        else:
            success = self.repository.update_joke_rating(joke_id, value)
            if not success:     
                if self.repository.get_joke_by_id(joke_id) is None:
                    raise ValueError(f"Joke with ID {joke_id} not found.")
                else:
                    raise RuntimeError(f"Failed to update rating for joke {joke_id}.")