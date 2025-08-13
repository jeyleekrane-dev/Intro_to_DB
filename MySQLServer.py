#!/usr/bin/env python3

import mysql.connector
from mysql.connector import errorcode

# MySQL connection settings
config = {
    'user': 'your_username',
    'password': 'your_password',
    'host': '127.0.0.1'
}

try:
    # Connect to MySQL
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()

    # Create the database directly
    cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Error: Access denied. Check your username and password.")
    else:
        print(f"Error connecting to the database: {err}")

finally:
    # Close the connection if it was successfully opened
    if 'cnx' in locals() and cnx.is_connected():
        cursor.close()
        cnx.close()
        print("Database connection closed.")
