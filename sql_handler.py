import sqlite3

db = {
    'Table': 'dad_jokes',
    'id': '_id',
    'post_id': 'post_id',
    'post_title': "title",
    'post_body': 'body',
    'author': 'author'
}

_db = sqlite3.connect('mydb.db')

_cursor = _db.cursor()

_cursor.execute("CREATE TABLE IF NOT EXISTS jokes (_id INTEGER PRIMARY KEY AUTOINCREMENT, post_id TEXT, title TEXT,"
                " body TEXT, author TEXT)")


def insert_joke(post_id, title, body, author):
    _cursor.execute('SELECT * FROM jokes WHERE post_id = "' + str(post_id) + '"')
    v = _cursor.fetchall()
    if len(v) is 0:
        _cursor.execute('INSERT INTO jokes(post_id, title, body, author) VALUES(?,?,?,?)',
                        (str(post_id), str(title), str(body), str(author)))
        _db.commit()
        print('inserted joke')
        return
    print("joke already exists")
    pass


def get_random_joke():
    _cursor.execute('SELECT * FROM jokes ORDER BY RANDOM() LIMIT 1')
    joke = _cursor.fetchone()
    if joke is None:
        return ['', '', '']
    return [joke[2], joke[3], joke[4]]
    pass

# def delete_all_row():
#     _cursor.execute("DELETE FROM jokes WHERE 1")
#     _db.commit()
