import sqlite3

conn = sqlite3.connect('db/example.db')
cur = conn.cursor()

cur.execute('''
INSERT INTO users (id, name, age) VALUES (?, ?, ?)
''', (1, 'Ernar', 22))
conn.commit()

cur.execute('SELECT * FROM users')
rows = cur.fetchall()
for row in rows:
    print(row)

conn.close()