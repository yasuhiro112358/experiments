import sqlite3
import os

class MemoryDB:
    def __init__(self, db_path="data/memory.db"):
        self.db_path = db_path
        os.makedirs(os.path.dirname(db_path), exist_ok=True)
        self.conn = sqlite3.connect(db_path)
        self.create_table()

    def create_table(self):
        with self.conn:
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS memory (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    conversation_id TEXT NOT NULL,
                    role TEXT NOT NULL,
                    content TEXT NOT NULL
                )
            """)

    def insert(self, conversation_id, role, content):
        with self.conn:
            self.conn.execute("""
                INSERT INTO memory (conversation_id, role, content)
                VALUES (?, ?, ?)
            """, (conversation_id, role, content))

    def get_messages(self, conversation_id):
        with self.conn:
            cursor = self.conn.execute("""
                SELECT role, content FROM memory
                WHERE conversation_id = ?
                ORDER BY id
            """, (conversation_id,))
            return [{"role": row[0], "content": row[1]} for row in cursor.fetchall()]