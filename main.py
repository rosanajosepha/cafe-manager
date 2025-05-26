from db import setup_database
# from menu import reset_menu
from inventory import get_low_stock, reset_inventory
from models import MenuItem, InventoryItem

def main():
    setup_database()
    # reset_menu()
    # reset_inventory()
    # print("Reset menu and inventory")

    # Add some test data
    if not MenuItem.exists("Latte"):
        latte = MenuItem("Latte", 4.50)
        latte.save()

    if not InventoryItem.exists("milk"):
        milk = InventoryItem("milk", 5)
        milk.save()

    # Display tables
    print("📋 MENU:")
    for item in MenuItem.get_all():
        print(item)

    print("\n📦 INVENTORY:")
    for item in InventoryItem.get_all():
        print(item)
    
    print("\n🚨 LOW STOCK:")
    for item in get_low_stock():
        print(item)
    

if __name__ == "__main__":
    main()