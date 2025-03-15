import sqlite3
import os
from typing import List, Dict

class MemoryDB:
    def __init__(self, db_path=None) -> None:
        if db_path is None:
            db_path = os.path.join(os.path.dirname(__file__), "../../data/memory.db")
        self.db_path = db_path
        os.makedirs(os.path.dirname(db_path), exist_ok=True)
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
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
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS personas (
                    id TEXT PRIMARY KEY,
                    name TEXT NOT NULL,
                    personality TEXT NOT NULL
                )
            """)

    def insert(self, conversation_id: str, speaker_id: str, listener_id: str, content: str) -> None:
        """
        会話履歴を記録する
        ※あとでメソッド名を変更する
        """
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
        
    def save_persona(self, persona_id: str, name: str, personality: str) -> None:
        with self.conn:
            self.conn.execute("""
                INSERT INTO personas (id, name, personality)
                VALUES (?, ?, ?)
            """, (persona_id, name, personality))

    def load_persona(self, persona_id: str) -> Dict[str, str]:
        with self.conn:
            cursor = self.conn.execute("""
                SELECT name, personality FROM personas
                WHERE id = ?
            """, (persona_id,))
            row = cursor.fetchone()
            if row:
                return {"name": row[0], "personality": row[1]}
            else:
                return None