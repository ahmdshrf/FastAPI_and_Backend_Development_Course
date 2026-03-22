import sqlite3


#Make a Connection to the database
connection = sqlite3.connect("sqlite.db")
cursor = connection.cursor()

#1. Create a table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS shipment (
    id INTEGER PRIMARY KEY,
    content TEXT,
    weight REAL,
    destination TEXT,
    shipment_status TEXT,
    zip_code INTEGER
)""")


connection.close()

    