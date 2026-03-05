#!/usr/bin/python3
"""
0. Get all states
Script that lists all states from the database hbtn_0e_0_usa
Arguments: mysql username, mysql password, database name
Connects to a MySQL server running on localhost at port 3306
Results are sorted in ascending order by states.id
"""

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()
