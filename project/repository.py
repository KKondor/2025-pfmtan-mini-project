import os
from typing import List, Optional
from dotenv import load_dotenv
import mysql.connector

class Joke:
    def __init__(self, id, text, rating):
        self.id = id
        self.text = text
        self.rating = rating
        self.setup = "" # just a placeholder, JokeService will seperate setup and punchline from text
        self.punchline = ""

load_dotenv() # load environment variables from .env

class JokeRepository:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            port=int(os.getenv("DB_PORT")),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )

    def get_joke_by_id(self, joke_id: int) -> Optional[Joke]: # Returns a Joke object or None if not found
        pass

    def get_jokes_list(self, sort_order: str = "desc", filter_type: str = "all") -> List[Joke]: # Returns a list of 5!!! Joke objects
        pass

    def update_joke_rating(self, joke_id: int, operating: int) -> bool: # Returns True if update was successful, False otherwise
        pass

    def close(self):
        self.conn.close()