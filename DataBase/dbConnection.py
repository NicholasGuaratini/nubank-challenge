import json
import sqlite3
from sqlite3 import Error
from Entities import CreateAccount


def create_connection():
    
    conn = None;
    try:
        conn = sqlite3.connect(':memory:') 
        print(sqlite3.version)
        return conn
    except Error as e:
        print(e)
    # finally:
    #     if conn:
    #         conn.close()

def create_table(conn):

    c = conn
    c.execute("""CREATE TABLE IF NOT EXISTS Account(
       ID_Account INTEGER PRIMARY KEY AUTOINCREMENT,
       Active_Card BOOLEAN,
       Available_Limit INTEGER);
    """)
    c.commit()
    print('Table created')

def insert_register(conn, activeCard, availableLimit):

    c = conn.cursor()

    c.execute('INSERT INTO Account (Active_Card, Available_Limit) VALUES (?,?)', (activeCard, availableLimit))
    
    conn.commit()
    print('Added data')

def select_register(conn):
    s = conn.cursor()
    s.execute("SELECT * FROM Account;")
    results = s.fetchall()
    return results
    conn.commit() 
