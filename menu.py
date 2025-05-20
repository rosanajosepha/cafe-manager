from db import get_connection

def reset_menu():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM menu")
    cursor.execute("DELETE FROM sqlite_sequence WHERE name='menu'")  # Resets ID to 1
    conn.commit()
    conn.close()
