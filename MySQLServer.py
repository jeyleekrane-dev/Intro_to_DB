#!/usr/bin/env python3

import mysql.connector
from mysql.connector import errorcode

# Configuration for the MySQL connection
config = {
    'user': 'your_username',  # Replace with your MySQL username
    'password': 'your_password',  # Replace with your MySQL password
    'host': '127.0.0.1'
}

# Name of the database to be created
DB_NAME = 'alx_book_store'


def create_database():
    """
    Connects to MySQL, creates the specified database if it doesn't exist,
    and handles connection errors.
    """
    try:
        # Establish connection to the MySQL server
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()

        # SQL query to create the database if it doesn't exist
        # Using a parameterized query to avoid SQL injection
        sql = "CREATE DATABASE IF NOT EXISTS {}".format(DB_NAME)

        try:
            print("Creating database {}...".format(DB_NAME))
            cursor.execute(sql)
            print("Database '{}' created successfully!".format(DB_NAME))
        except mysql.connector.Error as err:
            print("Failed creating database: {}".format(err))
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error: Access denied. Check your username and password.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Error: Database does not exist.")
        else:
            print("Error connecting to the database: {}".format(err))
    finally:
        # Close the cursor and connection if they were successfully created
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        if 'cnx' in locals() and cnx is not None:
            cnx.close()
            print("Database connection closed.")


if __name__ == '__main__':
    create_database()
