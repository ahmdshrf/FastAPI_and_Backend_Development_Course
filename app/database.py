import sqlite3
from typing import Any
from app.schemas import ShipmentCreate, ShipmentUpdate


class Database:
    def __init__(self):
        self.conn = sqlite3.connect("sqlite.db")
        self.cur = self.conn.cursor()
        # Create a table
        self.create_table()

    def create_table(self):
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS shipment (
            id INTEGER PRIMARY KEY,
            content TEXT,
            weight REAL,
            destination TEXT,
            shipment_status TEXT,
            zip_code INTEGER
        )""")
        self.conn.commit()

    def create_shipment(self, shipment: ShipmentCreate) -> int | None:
        self.cur.execute("""select max(id) from shipment""")
        max_id = self.cur.fetchone()
        new_id = max_id[0] + 1 if max_id[0] is not None else None
        self.cur.execute(
            """
            INSERT INTO shipment
            VALUES (:id, :content, :weight, :destination, :shipment_status, :zip_code)
        """,
            {
                "id": new_id,
                "content": shipment.content,
                "weight": shipment.weight,
                "destination": shipment.destination,
                "shipment_status": "placed",
                "zip_code": shipment.zip_code,
            },
        )
        self.conn.commit()
        return new_id

    def get_shipment(self, id: int) -> dict[str, Any] | None:
        self.cur.execute("SELECT * FROM shipment WHERE id = ?", (id,))
        row = self.cur.fetchone()
        if row:
            return {
                "id": row[0],
                "content": row[1],
                "weight": row[2],
                "destination": row[3],
                "shipment_status": row[4],
                "zip_code": row[5],
            }
        return None
    
    def get_latest_shipment(self) -> dict[str, Any] | None:
        self.cur.execute("SELECT * FROM shipment ORDER BY id DESC LIMIT 1")
        row = self.cur.fetchone()
        if row:
            return {
                "id": row[0],
                "content": row[1],
                "weight": row[2],
                "destination": row[3],
                "shipment_status": row[4],
                "zip_code": row[5],
            }
        return None

    def update_shipment(
        self, id: int, shipment: ShipmentUpdate
    ) -> dict[str, Any] | None:
        self.cur.execute(
            """
            UPDATE shipment 
            SET shipment_status = :shipment_status 
            SET CONTENT = :content
            SET weight = :weight
            SET destination = :destination
            SET zip_code = :zip_code
            WHERE id = :id
            """,
            {
                "shipment_status": shipment.shipment_status,
                "content": shipment.content,
                "weight": shipment.weight,
                "destination": shipment.destination,
                "zip_code": shipment.zip_code,
                "id": id
            },
        )
        self.conn.commit()
        return self.get_shipment(id)
    
    def delete_shipment(self, id: int) :
        self.cur.execute("DELETE FROM shipment WHERE id = ?", (id,))
        self.conn.commit()

    def close(self):
        if self.conn:
            self.conn.close()
            self.conn = None
            self.cursor = None


# 2. Add shipment data
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

# 3. Read a shipment by ID
# cursor.execute("SELECT * FROM shipment WHERE id = 12078")
# result = cursor.fetchall()
# print(result)

# 6. Delete a table
# cursor.execute("DROP TABLE shipment")
# connection.commit()
