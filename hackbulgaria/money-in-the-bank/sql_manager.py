import requests
import sqlite3
import re
import hashlib

from Client import Client

conn = sqlite3.connect("bank.db")
cursor = conn.cursor()


def create_clients_table():
    create_query = '''create table if not exists
        clients(id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT,
                password TEXT,
                balance REAL DEFAULT 0,
                message TEXT)'''

    cursor.execute(create_query)



def change_message(new_message, logged_user):
    cursor.execute('''UPDATE clients SET message = ? WHERE id = ?''',(new_message, logged_user.get_id()))
    conn.commit()
    logged_user.set_message(new_message)


def change_pass(new_pass, logged_user):
    cursor.execute('''UPDATE clients SET password = ? WHERE id = ?''',(new_pass, logged_user.get_id()))
    conn.commit()

def crypt_pass(password):
    hash_object = hashlib.sha1(password.encode())
    return hash_object.hexdigest()

def password_validator(password):
    pattern = "^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$"
    if re.findall(pattern, password):
        return True
    else:
        return False



def register(username, password):
    cursor.execute('''insert into clients (username, password) values (?, ?)''', (username, password))
    conn.commit()


def login(username, password):
    cursor.execute('''SELECT id, username, balance, message FROM clients WHERE username = ? AND password = ? LIMIT 1''',(username, password))
    user = cursor.fetchone()

    if(user):
        return Client(user[0], user[1], user[2], user[3])
    else:
        return False
