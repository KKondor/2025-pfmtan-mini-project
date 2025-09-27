import os
from dotenv import load_dotenv
import mysql.connector

class Joke:
    def __init__(self, id, text, rating):
        self.id = id
        self.text = text
        self.rating = rating

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

    def get_joke_by_id(self, joke_id):
        pass

    def get_jokes_list(self, sort_order, filter_type):
        pass

    def update_joke_rating(self, joke_id, operating):
        pass

    def close(self):
        self.conn.close()