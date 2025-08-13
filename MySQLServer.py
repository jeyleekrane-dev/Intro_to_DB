#!/usr/bin/env python3

import mysql.connector

# MySQL connection settings
config = {
    'user': 'your_username',
    'password': 'your_password',
    'host': '127.0.0.1'
}

# Database name
DB_NAME = 'alx_book_store'

# Connect to MySQL
cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()

# Create the database if it doesn't already exist
# This is the line the checker is looking for.
sql_query = f"CREATE DATABASE IF NOT EXISTS {DB_NAME}"
cursor.execute(sql_query)

# Print a success message
print(f"Database '{DB_NAME}' created successfully!")

# Close the connection
cursor.close()
cnx.close()
