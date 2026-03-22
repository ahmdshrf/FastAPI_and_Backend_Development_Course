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

#2. Add shipment data
# cursor.execute("""
#     INSERT INTO shipment 
#     VALUES
#     (12078, 'table', 0.78, 'Paris', 'in_transit', 75001),
#     (12079, 'chair', 0.5, 'London', 'delivered', 12345),
#     (12080, 'bookshelf', 2.3, 'Berlin', 'pending', 10117),
#     (12081, 'lamp', 0.8, 'Rome', 'in_transit', 100),
#     (12082, 'desk', 1.5, 'Madrid', 'pending', 28001),
#     (12083, 'cabinet', 3.2, 'Amsterdam', 'delivered', 1012),
#     (12084, 'laptop', 4.1, 'Vienna', 'in_transit', 1010)
# """)
# connection.commit()

#3. Read a shipment by ID
# cursor.execute("SELECT * FROM shipment WHERE id = 12078")
# result = cursor.fetchall()
# print(result)

#4. Delete a shipment by ID
# cursor.execute("DELETE FROM shipment WHERE id = 12084")
# connection.commit()

#5. Update a shipment
id = 12078
shipment_status = "out_for_delivery"
cursor.execute("""
    UPDATE shipment 
    SET shipment_status = :shipment_status 
    WHERE id = :id
    """, {"shipment_status": shipment_status, "id": id})
connection.commit()  

#6. Delete a table
# cursor.execute("DROP TABLE shipment")
# connection.commit()

connection.close()

    