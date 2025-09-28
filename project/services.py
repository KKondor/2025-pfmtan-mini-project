from repository import Joke, JokeRepository
from typing import Optional, List
import random

class JokeService:
    def __init__(self, repository: JokeRepository):
        self.repository = repository

    def generate_joke(self) -> Joke:
        random_id = random.randint(1, 700)
        joke = self.repository.get_joke_by_id(random_id)
        if joke:
            if "?" in joke.text:
                parts = joke.text.split("?", 1) # split on first "?"
                joke.setup = parts[0] + "?" 
                joke.punchline = parts[1].strip() 
            else:
                joke.setup = joke.text
                joke.punchline = ""
            return joke
        else:
            raise ValueError("No joke found with the generated ID.")
        
    def get_leaderboard(self, sort_order: str = "rating", filter_type: str = "all") -> list[Joke]:
        jokes = self.repository.get_jokes_list(sort_order, filter_type)
        for joke in jokes:
            if "?" in joke.text:
                parts = joke.text.split("?", 1)
                joke.setup = parts[0] + "?"
                joke.punchline = parts[1].strip()
            else:
                joke.setup = joke.text
                joke.punchline = ""
        return jokes
    
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