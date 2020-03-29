#!/usr/bin/python3
# script that lists all states from the database hbtn_0e_0_usa

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",port=3306,passwd="argv[2]",
                         db="argv[3]",user="argv[1]")
    c = db.cursor()
    c = c.execute("""select * from states ORDER BY id asc """)
    row = c.fetchall()
    for r in row:
        print(r)
    c.close()
    db.close()
