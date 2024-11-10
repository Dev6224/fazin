import pickle

# File path for storing the supplier data (in binary format)
SUPPLIER_FILE = "suppliers.dat"

# Function to load all supplier data from the binary file
def load_suppliers():
    try:
        with open(SUPPLIER_FILE, "rb") as file:
            return pickle.load(file)  # Load the entire dictionary of suppliers
    except FileNotFoundError:
        return {}  # Return an empty dictionary if the file doesn't exist
    except Exception as e:
        print(f"Error loading data: {e}")
        return {}

# Function to save the dictionary of suppliers to the binary file
def save_suppliers(suppliers):
    try:
        with open(SUPPLIER_FILE, "wb") as file:
            pickle.dump(suppliers, file)  # Save the entire dictionary
    except Exception as e:
        print(f"Error saving data: {e}")

# Function to add a new supplier
def add_supplier():
    # Load existing suppliers from file
    suppliers = load_suppliers()

    supplier_id = input("Enter the supplier ID: ")
    name = input("Enter the supplier name: ")
    contact = input("Enter the supplier contact (phone/email): ")
    product = input("Enter the product supplied: ")

    # Add the new supplier to the dictionary
    suppliers[supplier_id] = {
        'name': name,
        'contact': contact,
        'product': product
    }

    # Save the updated suppliers data back to the file
    save_suppliers(suppliers)
    print("Supplier added successfully.")

# Function to view all suppliers
def view_suppliers():
    # Load suppliers from file
    suppliers = load_suppliers()

    if not suppliers:
        print("No suppliers found.")
    else:
        print("\nAll Suppliers:")
        for supplier_id, details in suppliers.items():
            print(f"Supplier ID: {supplier_id}")
            print(f"Name: {details['name']}")
            print(f"Contact: {details['contact']}")
            print(f"Product Supplied: {details['product']}\n")

# Function to modify an existing supplier
def modify_supplier():
    # Load the suppliers from file
    suppliers = load_suppliers()

    supplier_id = input("Enter the supplier ID to modify: ")

    if supplier_id in suppliers:
        print(f"Current details for supplier ID {supplier_id}:")
        print(f"Name: {suppliers[supplier_id]['name']}")
        print(f"Contact: {suppliers[supplier_id]['contact']}")
        print(f"Product: {suppliers[supplier_id]['product']}")

        name = input("Enter the new name (leave blank to keep current): ")
        contact = input("Enter the new contact (leave blank to keep current): ")
        product = input("Enter the new product (leave blank to keep current): ")

        if name:
            suppliers[supplier_id]['name'] = name
        if contact:
            suppliers[supplier_id]['contact'] = contact
        if product:
            suppliers[supplier_id]['product'] = product

        # Save the updated suppliers back to the file
        save_suppliers(suppliers)
        print(f"Supplier ID {supplier_id} updated successfully.")
    else:
        print(f"Supplier ID {supplier_id} not found.")

# Function to delete a supplier
def delete_supplier():
    # Load suppliers from file
    suppliers = load_suppliers()

    supplier_id = input("Enter the supplier ID to delete: ")

    if supplier_id in suppliers:
        del suppliers[supplier_id]  # Remove the supplier from the dictionary

        # Save the updated suppliers data back to the file
        save_suppliers(suppliers)
        print(f"Supplier ID {supplier_id} deleted successfully.")
    else:
        print(f"Supplier ID {supplier_id} not found.")

# Menu for interacting with the supplier system
def supplier_menu():
    while True:
        print("\nSupplier Management Menu:")
        print("1. Add Supplier")
        print("2. View All Suppliers")
        print("3. Modify Supplier Info")
        print("4. Delete Supplier")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_supplier()  # Add a new supplier
        elif choice == '2':
            view_suppliers()  # View all suppliers
        elif choice == '3':
            modify_supplier()  # Modify existing supplier info
        elif choice == '4':
            delete_supplier()  # Delete a supplier
        elif choice == '5':
            break  # Exit the menu
        else:
            print("Invalid choice! Please try again.")
