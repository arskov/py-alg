import json
import dataclasses
import sys
from dataclasses import dataclass
import sqlite3

@dataclass
class User:
    first_name: str
    last_name: str
    age: int

if __name__ == "__main__":
    with sqlite3.connect(sys.path[0] + "/example.db") as conn:
        curs = conn.cursor()
        curs.execute("CREATE TABLE IF NOT EXISTS \
            users ( \
                id INTEGER PRIMARY KEY, \
                first_name VARCHAR(255), \
                last_name VARCHAR(255), \
                age INTEGER \
            )")
        d = User("Ivan", "Ivanov", 33)
        curs.execute("INSERT INTO users(first_name, last_name, age) VALUES(?, ?, ?)", dataclasses.astuple(d))
        for row in curs.execute("SELECT * FROM users"):
            print(row)
