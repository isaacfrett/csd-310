# Isaac Frett 11/26/2022 Module 8.2 Assignment: Movies: Update & Deletes

import mysql.connector
from mysql.connector import errorcode

# config settings in order to connect to MySQL
config = {
    "user": "root",
    "password": "root",
    "host": "127.0.0.1",
    "database": "movies",
    "raise_on_warnings": True
}

# funcion to display our output after changes to the tables are made
def show_films(cursor, title):
    cursor.execute("SELECT film_name as Name, film_director as Director, genre_name as Genre, studio_name as 'Studio Name' from film INNER JOIN genre ON film.genre_id=genre.genre_id INNER JOIN studio ON film.studio_id=studio.studio_id") 

    films = cursor.fetchall()

    print("\n -- {} --".format(title))

    for film in films:
        print("Film Name: {}\nDirector: {}\nGenre Name ID: {}\nStudio Name: {}\n".format(film[0], film[1], film[2], film[3]))


# Try, Except, Finally block to connect to DB, and call the show_films function
try:
    input("\n Press any key to continue...\n")
    db = mysql.connector.connect(**config)
    cursor = db.cursor()

    show_films(cursor, "DISPLAYING FILMS")

    # Adding a new studio, genre, and film to create a new record
    cursor.execute("INSERT INTO studio (studio_name, studio_id) VALUES ('Marvel Studios', '4')")
    cursor.execute("INSERT INTO genre (genre_name, genre_id) VALUES ('Action', '4')")
    cursor.execute("INSERT INTO film (film_id, film_name, film_director, film_releaseDate, film_runtime, studio_id, genre_id) VALUES ('4', 'Iron Man', 'Jon Favreau', '2008', '126', '4', '4')")
    show_films(cursor, "DISPLAYING FILMS AFTER INSERT")

    # Updating the genre of Alien to Horror
    cursor.execute("UPDATE film SET genre_id = '1' WHERE film_name = 'Alien'")
    show_films(cursor, "DISPLAYING FILMS AFTER UPDATE- Changed Alien to Horror")

    # Deleteing the movie Gladiator
    cursor.execute("DELETE FROM film WHERE film_name = 'Gladiator'")
    show_films(cursor, "DISPLAYING FILMS AFTER DELETE")
    input("\n Press any key to continue...\n")

# Except to raise any errors
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")
    else:
        print(err)

# close the DB
finally:
    db.commit()
    db.close()