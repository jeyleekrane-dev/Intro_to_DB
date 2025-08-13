#!/usr/bin/env python3

import mysql.connector

# MySQL connection settings
config = {
    'user': 'your_username',
    'password': 'your_password',
    'host': '127.0.0.1'
}

# Connect to MySQL
cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()

# Create the database directly
cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

# Print a success message
print("Database 'alx_book_store' created successfully!")

# Close the connection
cursor.close()
cnx.close()
