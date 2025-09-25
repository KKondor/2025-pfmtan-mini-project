#!/usr/bin/env python3
import mysql.connector #ezt be kell importálni hogy tudj csatlakozni az adatbázishoz



def main():
    # ezek a szerver csatlakozásához szükséges adatok
    conn = mysql.connector.connect(
        host="mainline.proxy.rlwy.net",
        port=38653,
        user="root",
        password="uMylKlJvWQlMPPPcuEulFDHMlEmIVWRw",
        database="railway"
    )

    get_joke = conn.cursor()
    get_joke.execute("SELECT get_joke_by_id(5)") # az adatbázisban előre megírt függvény ami visszaad egy viccet id alapján
    joke = get_joke.fetchone()[0]
    print("A vicc:", joke)
    get_joke.close()



    get_jokes = conn.cursor()
    sort_order='asc' #lehet:'asc', 'desc', 'rating'
    filter_type="animal" #lehet: 'all', 'informatics', 'animal', 'weather', 'mom', 'dad', 'school', 'pun'
    get_jokes.execute("CALL get_jokes_list(%s,%s)",(sort_order,filter_type)) # az adatbázisban előre megírt függvény ami visszaad egy rendezett szürt listát
    jokes=get_jokes.fetchall()
    print("viccek szürve és rendezve: ",jokes)
    get_jokes.close()

    update_joke_rating = conn.cursor()
    joke_idx = 3
    operating = 'subtract'  # lehet: add, subtract
    update_joke_rating.execute("CALL update_joke_rating(%s,%s)", (joke_idx,operating))  # az adatbázisban előre megírt függvény ami módisítja az értékelést
    conn.commit()
    update_joke_rating.close()


    conn.close()


if __name__ == "__main__":
    main()