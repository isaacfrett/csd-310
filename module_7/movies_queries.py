# Isaac Frett 11/22/2022 Module 7.2 Assignment: Movies: Table Queries

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

# Try, Except, Finally block to connect to DB, and run the four queries while printing out the return data
try:
    db = mysql.connector.connect(**config)
    print("\nDatabase user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))
    input("\n\n Press any key to continue...")

    cursor = db.cursor()
    
    cursor.execute("SELECT * FROM studio")
    data_fetch = cursor.fetchall()
    print("\n-- DISPLAYING Studio RECORDS --")
    for data in data_fetch:
        print("Studio ID: {}\nStudio Name: {}".format(data[0], data[1]))


    cursor.execute("SELECT * FROM genre")
    data_fetch = cursor.fetchall()
    print("\n-- DISPLAYING Genre RECORDS --")
    for data in data_fetch:
        print("Genre ID: {}\nGenre Name: {}".format(data[0], data[1]))


    cursor.execute("SELECT film_name, film_runtime FROM film WHERE film_runtime < 120")
    data_fetch = cursor.fetchall()
    print("\n-- DISPLAYING Short Film RECORDS --")
    for data in data_fetch:
        print("Film Name: {}\nRuntime: {}".format(data[0], data[1]))


    cursor.execute("SELECT film_name, film_director FROM film ORDER BY film_director")
    data_fetch = cursor.fetchall()
    print("\n-- DISPLAYING Director RECORDS in Order --")
    for data in data_fetch:
        print("Film Name: {}\nDirector: {}".format(data[0], data[1]))
    
    input("\n\n Press any key to continue...")
   
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
    db.close()