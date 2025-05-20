from db import get_connection

class BaseModel:
    table = None # to be set in child class

    def __init__(self, name):
        self.name = name

    def save(self):
        raise NotImplementedError("Subclasses should implement their own save() method.")

    @classmethod
    def get_all(cls):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {cls.table}")
        items = cursor.fetchall()
        conn.close()
        return items
    
    ''' Checks if the item already exists in the menu/inventory'''
    @classmethod
    def exists(cls, name):
        conn = get_connection()
        cursor = conn.cursor()

        if cls.table == "menu":
            cursor.execute(f"SELECT * FROM {cls.table} WHERE name = ?", (name,))
        elif cls.table == "inventory":
            cursor.execute(f"SELECT * FROM {cls.table} WHERE ingredient = ?", (name,))
        
        result = cursor.fetchone()
        conn.close()
        return result is not None

# create MenuItem child
class MenuItem(BaseModel):
    table = "menu"

    def __init__(self, name, price):
        super().__init__(name)
        self.price = price

    # adds the item to the Menu
    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO menu {self.__class__.table} (name, price) VALUES (?, ?)", (self.name, self.price))
        conn.commit()
        conn.close()

# create InventoryItem child
class InventoryItem(BaseModel):
    table = "inventory"
    
    def __init__(self, name, quantity):
        super().__init__(name)
        self.quantity = quantity

    # adds the ingredient to the Inventory
    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO {self.__class__.table} (name, quantity) VALUES (?, ?)", (self.name, self.quantity))
        conn.commit()
        conn.close()