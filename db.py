import sqlite3

def get_connection():
    return sqlite3.connect("database.db");

def setup_database():
    conn = get_connection()
    cursor = conn.cursor()

    # Menu table
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS menu (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE,
            price REAL NOT NULL
        )
    """
    )

    # Inventory table
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS inventory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ingredient TEXT UNIQUE,
            quantity INTEGER NOT NULL
        )
    """
    )

    # Orders table
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS inventory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            item_name TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """
    )

    conn.commit()
    conn.close()