#!/usr/bin/python3

import MySQLdb
import os

# Read environment variables
mysql_user = os.environ.get('HBNB_MYSQL_USER')
mysql_password = os.environ.get('HBNB_MYSQL_PWD')
mysql_host = os.environ.get('HBNB_MYSQL_HOST')
mysql_database = os.environ.get('HBNB_MYSQL_DB')

try:
    # Connect to the MySQL database
    connection = MySQLdb.connect(
        host=mysql_host,
        port=3306,
        user=mysql_user,
        password=mysql_password,
        database=mysql_database,
        charset="utf8"
    )

    print("Connection to MySQL database successful!")

finally:
    # Close the database connection
    connection.close()

