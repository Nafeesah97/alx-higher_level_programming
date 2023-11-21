#!/usr/bin/python3
"""
Importing the necessary libraries
"""
import sys
import MySQLdb
"""
This module is to list all the rows that state starts with N
It lists it in ascending order by states.id
Author: Nafeesah
"""
if __name__ == "__main__":
    arg = sys.argv
    mysql_username = arg[1]
    mysql_password = arg[2]
    database_name = arg[3]
    word = arg[4]

    db = MySQLdb.connect(
            host='localhost', user=mysql_username, passwd=mysql_password,
            db=database_name, port=3306
            )
    cursor = db.cursor()
    cursor.execute(
            "SELECT id, name FROM states WHERE BINARY name = '{}'\
            ORDER BY id".format(word)
            )
    rows = cursor.fetchall()
    for row in rows:
        print('{}'.format(row))
    cursor.close()
    db.close()
