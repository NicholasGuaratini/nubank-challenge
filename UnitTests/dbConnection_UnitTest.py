import sqlite3
from sqlite3 import Error
from DataBase import dbConnection


def dbConnectionCreate_UnitTest():
    conn = None;
    try:
        conn = sqlite3.connect(':memory:') 
        print(sqlite3.version)
        print(True)
    except Error as e:
        print(False)

def create_table(conn):

	try:
	    c = conn
	    c.execute("""CREATE TABLE IF NOT EXISTS Account(
	       ID_Account INTEGER PRIMARY KEY AUTOINCREMENT,
	       Active_Card BOOLEAN,
	       Available_Limit INTEGER);
	    """)
	    c.commit()
	    print('Table created')
	    print(True)
    except Error as e:
    	print(False)
    	 
def insert_UnitTest():

	try:
		activeCard = True
		availableLimit = 100

		c = conn.cursor()

    	c.execute('INSERT INTO Account (Active_Card, Available_Limit) VALUES (?,?)', (activeCard, availableLimit))
    	conn.commit()
    	
    	print(True)
	except Error as e:
			print(False)