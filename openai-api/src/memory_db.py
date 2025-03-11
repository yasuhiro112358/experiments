import sqlite3
import os
from typing import List, Dict

class MemoryDB:
    def __init__(self, db_path="data/memory.db") -> None:
        self.db_path = db_path
        os.makedirs(os.path.dirname(db_path), exist_ok=True)
        self.conn = sqlite3.connect(db_path)
        self.create_table()

    def create_table(self) -> None:
        with self.conn:
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS memory (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    conversation_id TEXT NOT NULL,
                    speaker_id TEXT NOT NULL,
                    listener_id TEXT NOT NULL,
                    content TEXT NOT NULL
                )
            """)

    def insert(self, conversation_id: str, speaker_id: str, listener_id: str, content: str) -> None:
        with self.conn:
            self.conn.execute("""
                INSERT INTO memory (conversation_id, speaker_id, listener_id, content)
                VALUES (?, ?, ?, ?)
            """, (conversation_id, speaker_id, listener_id, content))

    def get_messages(self, conversation_id) -> List[Dict[str, str]]:
        with self.conn:
            cursor = self.conn.execute("""
                SELECT speaker_id, listener_id, content FROM memory
                WHERE conversation_id = ?
                ORDER BY id
            """, (conversation_id,))
            return [{"speaker_id": row[0], "listener_id": row[1], "content": row[2]} for row in cursor.fetchall()]