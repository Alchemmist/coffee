import sqlite3
from data_types import CoffeeInf


def get_all_coffee(connection: sqlite3.Connection) -> list:
    cur = connection.cursor()
    result = cur.execute("select * from coffee").fetchall()
    return result


def edit_coffee(connection: sqlite3.Connection, data: CoffeeInf, ind: int) -> None:
    cur = connection.cursor()
    comand = (
        f"update coffee "
        f"set sort = '{data.sort}', "
        f"    degree_of_roasting = '{data.degree_of_roasting}', "
        f"    kind = '{data.kind.value}', "
        f"    taste_description = '{data.taste_description}', "
        f"    price = {data.price}, "
        f"    volume = {data.volume} "
        f"where id = {ind};"
    )

    cur.execute(comand).fetchall()
    connection.commit()


def add_coffee(connection: sqlite3.Connection, data: CoffeeInf) -> None:
    cur = connection.cursor()
    comand = (
        f"insert into coffee (sort, degree_of_roasting, kind, taste_description, "
        f"price, volume) values "
        f"('{data.sort}', '{data.degree_of_roasting}', '{data.kind.value}', "
        f"'{data.taste_description}', {data.price}, {data.volume});"
    )

    cur.execute(comand).fetchall()
    connection.commit()
