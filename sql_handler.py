import sqlite3

db = {
    'Table': "",
    'id': "",
    'main_field': ""
}

_db = sqlite3.connect('mydb.db')

_cursor = _db.cursor()
