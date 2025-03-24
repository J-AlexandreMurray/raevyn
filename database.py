import sqlite3

DB_NAME = "raevyn.db"

def initialize_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS worlds (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT
        )
    ''')
    conn.commit()
    conn.close()

def add_world(name, description):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO worlds (name, description) VALUES (?, ?)", (name, description))
    conn.commit()
    conn.close()

def get_worlds():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM worlds")
    worlds = cursor.fetchall()
    conn.close()
    return worlds

initialize_db()