import sqlite3

conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE users(id INTEGER PRIMARY KEY, name TEXT,
                       monthly_salary INTEGER, yearly_bonus INTEGER, position TEXT)
''')

conn.commit()
