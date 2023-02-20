import sqlite3


def get_all_coffee(connection: sqlite3.Connection) -> list:
    cur = connection.cursor()
    result = cur.execute("select * from coffee").fetchall()
    return result
