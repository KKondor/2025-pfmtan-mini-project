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
        cursor = self.conn.cursor()
        try:
            cursor.callproc('get_joke_by_id', (joke_id,))

            result = None
            for result_set in cursor.stored_results():
                result = result_set.fetchone()
                break

            if result:
                joke = Joke(id=result[0], text=result[1], rating=result[2])
                return joke
            else:
                return None
            
        finally:
            cursor.close()

    def get_jokes_list(self, sort_order: str = "rating", filter_type: str = "all") -> List[Joke]: # Returns a list of 5!!! Joke objects
        cursor = self.conn.cursor()
        jokes_list: List[Joke] = []
        try:

            cursor.callproc('get_jokes_list', (sort_order, filter_type))

            for result_set in cursor.stored_results():
                results = result_set.fetchmany(5)

                for row in results:
                    jokes_list.append(Joke(id=row[0], text=row[1], rating=row[2]))

                break

            return jokes_list

        finally:
            cursor.close()

    def update_joke_rating(self, joke_id: int, operating: int) -> bool: # Returns True if update was successful, False otherwise
        cursor = self.conn.cursor()

        if operating == 1:
            operation = 'add'
        elif operating == -1:
            operation = 'subtract'


        try:
            cursor.callproc('update_joke_rating', (joke_id, operation))
            self.conn.commit()

            return True

        except Exception as e:

            self.conn.rollback()
            return False

        finally:
            cursor.close()

    def close(self):
        self.conn.close()
