import sqlite3

# Set a connection and a cursor
connection = sqlite3.connect("data.db")
cursor = connection.cursor()

# Query data
cursor.execute("SELECT * FROM events WHERE date='2023.11.17'")
rows = cursor.fetchall()
print(rows)

cursor.execute("SELECT * FROM events WHERE date='2023.12.31'")
rows = cursor.fetchall()
print(rows)

# Insert new rows
new_rows = [('Cats', 'Cats City', '2023.07.12'),
            ('Dogs', 'Dogs CIty', '2023.05.28')]

cursor.executemany("INSERT INTO events VALUES(?,?,?)", new_rows)
connection.commit()

# cursor.execute("SELECT * FROM events")
# rows = cursor.fetchall()
# print(rows)
