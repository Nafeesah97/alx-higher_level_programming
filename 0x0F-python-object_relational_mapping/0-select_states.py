#!/usr/bin/python3
"""
Importing the necessary libraries
"""
import sys
import MySQLdb
"""
This module is to list all the rows in the state
It lists it in ascending order by states.id
Author: Nafeesah
"""
arg = sys.argv
mysql_username = arg[0]
mysql_password = arg[1]
database_name = arg[2]

db = MySQLdb.connect(host=localhost, user=mysql_username, passwd=mysql_password, db=database_name, port=3306)
cursor = db.cursor()
cursor.execute("SELECT id, name FROM state ORDER BY id")
rows = cursor.fetchall()
for row in rows:
    for col in row:
        print("{}".format(col))
    print("\n")

cursor.close()
db.close()