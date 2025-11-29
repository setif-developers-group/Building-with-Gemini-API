import sqlite3
from datetime import datetime

class Database:
    def __init__(self, db_path="chat_history.db"):
        self.db_path = db_path
        self.init_db()

    def init_db(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                role TEXT,
                content TEXT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()
        conn.close()

    def add_message(self, user_id, role, content):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO messages (user_id, role, content) VALUES (?, ?, ?)", (user_id, role, content))
        conn.commit()
        conn.close()

    def get_history(self, user_id, limit=10):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT role, content FROM messages WHERE user_id = ? ORDER BY timestamp DESC LIMIT ?", (user_id, limit))
        rows = cursor.fetchall()
        conn.close()
        # Return in chronological order
        return [{"role": row[0], "content": row[1]} for row in reversed(rows)]
