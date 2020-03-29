#!/usr/bin/python3
# script that lists all states from the database hbtn_0e_0_usa

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1]
                         ,passwd=argv[2], db=argv[3])
    c = db.cursor()
    c.execute("select * from cities LEFT JOIN states ON cities.state_id = states.id  ORDER BY cities.id ASC")
    for r in c.fetchall():
        print(r)
    c.close()
    db.close()
