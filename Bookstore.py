import csv

INVENTORY_FILE = 'inventory.csv'

# Load inventory from file
def load_inventory():
    inventory = {}
    try:
        with open(INVENTORY_FILE, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                inventory[row['id']] = {
                    'title': row['title'],
                    'author': row['author'],
                    'price': float(row['price']),
                    'stock': int(row['stock'])
                }
    except FileNotFoundError:
        pass
    return inventory

# Save inventory to file
def save_inventory(inventory):
    with open(INVENTORY_FILE, mode='w', newline='') as file:
        fieldnames = ['id', 'title', 'author', 'price', 'stock']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for book_id, data in inventory.items():
            row = {'id': book_id, **data}
            writer.writerow(row)

# Add a new book
def add_book(inventory):
    book_id = input("Enter Book ID: ")
    if book_id in inventory:
        print("Book ID already exists.")
        return
    title = input("Enter Title: ")
    author = input("Enter Author: ")
    price = float(input("Enter Price: "))
    stock = int(input("Enter Stock: "))
    inventory[book_id] = {'title': title, 'author': author, 'price': price, 'stock': stock}
    print("Book added successfully.")

# Sell a book
def sell_book(inventory):
    book_id = input("Enter Book ID to sell: ")
    if book_id in inventory:
        if inventory[book_id]['stock'] > 0:
            inventory[book_id]['stock'] -= 1
            print(f"Sold 1 copy of '{inventory[book_id]['title']}'.")
        else:
            print("Out of stock.")
    else:
        print("Book not found.")

# View inventory
def view_inventory(inventory):
    print("\n--- Inventory ---")
    for book_id, data in inventory.items():
        print(f"ID: {book_id}, Title: {data['title']}, Author: {data['author']}, Price: ${data['price']}, Stock: {data['stock']}")
    print("----------------\n")

# Search for a book
def search_book(inventory):
    title = input("Enter title to search: ").lower()
    found = False
    for book_id, data in inventory.items():
        if title in data['title'].lower():
            print(f"ID: {book_id}, Title: {data['title']}, Author: {data['author']}, Price: ${data['price']}, Stock: {data['stock']}")
            found = True
    if not found:
        print("No matching books found.")

# Main program loop
def main():
    inventory = load_inventory()
    while True:
        print("\n1. Add Book\n2. Sell Book\n3. View Inventory\n4. Search Book\n5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_book(inventory)
        elif choice == '2':
            sell_book(inventory)
        elif choice == '3':
            view_inventory(inventory)
        elif choice == '4':
            search_book(inventory)
        elif choice == '5':
            save_inventory(inventory)
            print("Exiting and saving data.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
