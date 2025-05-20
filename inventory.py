from db import get_connection

def get_low_stock(threshold=3):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM inventory WHERE quantity <= ?", (threshold,))
    rows = cursor.fetchall()
    conn.close()
    return rows

def reset_inventory():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM inventory")
    cursor.execute("DELETE FROM sqlite_sequence WHERE name='inventory'")  # Resets ID to 1
    conn.commit()
    conn.close()