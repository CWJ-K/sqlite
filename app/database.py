import sqlite3

connection = sqlite3.connect('data.db')
connection.row_factory = sqlite3.Row # without this one, result of cursor is tuple (use index to identify column)


def create_table():
    with connection:
        connection.execute("DROP TABLE IF EXISTS dictionary;")
        connection.execute("CREATE TABLE IF NOT EXISTS dictionary (date TEXT, vocabulary TEXT, sentence TEXT);")


def add_entry(entry_date, entry_vocabulary, entry_sentence):
    with connection:
        connection.execute(
            "INSERT INTO dictionary VALUES (?, ?, ?);", (entry_date, entry_vocabulary, entry_sentence)
        )


def get_entries():
    cursor = connection.execute("SELECT date, vocabulary, sentence FROM dictionary;")
    return cursor