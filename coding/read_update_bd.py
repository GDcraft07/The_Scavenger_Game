import sqlite3
import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "best_socer.db")


def read_table():
    sqlite_connection = sqlite3.connect(db_path)
    cursor = sqlite_connection.cursor()

    sqlite_select_query = """SELECT * from result"""
    cursor.execute(sqlite_select_query)
    records = cursor.fetchall()
    cursor.close()
    if sqlite_connection:
        sqlite_connection.close()
    return records[0][1]


def update_table(result):
    sqlite_connection = sqlite3.connect(db_path)
    cursor = sqlite_connection.cursor()
    sql_update_query = f"""Update result set best_result = {str(result)} where id = 1"""
    cursor.execute(sql_update_query)
    sqlite_connection.commit()
    cursor.close()
    if sqlite_connection:
        sqlite_connection.close()
