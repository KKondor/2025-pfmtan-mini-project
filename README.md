# Joke Portal

A simple web application where users can get random jokes from a database, like or dislike them, and view a leaderboard of the top-rated jokes.

## Features

- Random Jokes – Press a button to get a random joke from the backend.

- Like & Dislike – Users can rate jokes to help track popularity.

- Leaderboard – Displays the highest-rated jokes.

- Backend Support – Jokes and ratings are stored in a database.


## Usage

1. **Set up the database**
   - Create a new PostgreSQL instance on [Railway](https://railway.app/).
   - Create a database named `jokes` with the following table:

     ```sql
     CREATE TABLE jokes (
       idx SERIAL PRIMARY KEY,
       joke_text TEXT NOT NULL,
       rating INT DEFAULT 0,
       joke_type VARCHAR(50)
     );
     ```
     This is the example of how a text looks like:
     
     *Why did the student write in pencil?To erase the evidence.*
     
     The "?" is needed for the backend to split the joke into setup and punchline.

   - Import the provided SQL file (with stored procedures) into the database.

     ```bash
     mysql -h <DB_HOST> -P <DB_PORT> -u <DB_USER> -p <DB_NAME> < "project/msql stored procedures.sql".sql
     ```

2. **Configure environment variables**  
   - Create a `.env` file in the project root with the following template and fill in your Railway database credentials:

     ```env
     DB_HOST=mainline.proxy.rlwy.net
     DB_PORT=5432
     DB_USER=yourusername
     DB_PASSWORD=yourpassword
     DB_NAME=railway
     ```

3. **Install dependencies**  
   Make sure you have Python installed. Then run:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app**  
   Start the application with:

   ```bash
   python project/app.py
   ```

4. **Open the website**  
   Paste the url from the console in a browser and enjoy.
