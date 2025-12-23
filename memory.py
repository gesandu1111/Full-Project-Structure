import sqlite3
from config import DB_NAME

# Initialize memory DB
conn = sqlite3.connect(DB_NAME, check_same_thread=False)
c = conn.cursor()
c.execute('''
CREATE TABLE IF NOT EXISTS memory (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    role TEXT,
    content TEXT
)
''')
conn.commit()

def add_message(role, content):
    c.execute("INSERT INTO memory (role, content) VALUES (?, ?)", (role, content))
    conn.commit()

def get_recent_messages(limit):
    c.execute("SELECT role, content FROM memory ORDER BY id DESC LIMIT ?", (limit,))
    rows = c.fetchall()
    return [{"role": role, "content": content} for role, content in reversed(rows)]

def clear_memory():
    c.execute("DELETE FROM memory")
    conn.commit()
