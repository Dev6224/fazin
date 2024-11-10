import mysql.connector
from fcsv import *
 DB = mysql.connector.connect(host="localhost", user="root", password="tiger")
C = DB.cursor()

def database():
    # Create the database
    C.execute("CREATE DATABASE IF NOT EXISTS sportsstore")
    C.execute("USE sportsstore")

def tablesport():
    # Create the table
    create_table_query = """
    CREATE TABLE IF NOT EXISTS store (
        regno INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(15),
        item_no INT,
        sportevent VARCHAR(15),
        quantity INT,
        price INT
    )
    """
    C.execute(create_table_query)

def buyt():
    item_no = int(input("Enter item ID: "))
    sportitem = input("Enter sport item: ")
    sportevent = input("Enter sport event: ")
    quantity = int(input("Enter quantity: "))
    brand = input("Enter brand name: ")
    price = int(input("Enter the price: "))

    # Insert the data into the table using placeholders
    insert_query = """
    INSERT INTO store (item_no, sportevent, quantity, username, price) 
    VALUES (%s, %s, %s, %s, %s)
    """
    C.execute(insert_query, (item_no, sportitem, quantity, brand, price))
    DB.commit()
    buy(item_no, quantity)
    m = get_last_record()
    add_bill_review(m)
 
    print("\n")
    print("++++++++++++++++++++++++SUCCESSFULLY ADDED++++++++++++++++++++++++")

def delete():
    bb = input("Are you sure you want to delete all records? (Y/N): ").upper()
    if bb == "Y":
        C.execute("DELETE FROM store")
        DB.commit()
        print("All records deleted successfully!")

def get_last_record():
    # Query to fetch the last record by sorting by regno in descending order
    query = "SELECT * FROM store ORDER BY regno DESC LIMIT 1"
    
    # Execute the query
    C.execute(query)
    
    # Fetch the result
    last_record = C.fetchone()
    
    if last_record:
        # Print the last record if it exists
        print(f"regno: {last_record[0]}, username: {last_record[1]}, item_no: {last_record[2]}, "
              f"sportevent: {last_record[3]}, quantity: {last_record[4]}, price: {last_record[5]}")
        return(last_record[0])
    else:
        print("No records found.")

        return None



def listofitems():
    print("1 - Item No, 2 - Sport Item, 3 - Sport Event, 4 - Brand")
    k = int(input("Want to see products ordered by (1, 2, 3, 4): "))

    if k == 1:
        C.execute("SELECT * FROM store ORDER BY item_no")
    elif k == 2:
        C.execute("SELECT * FROM store ORDER BY sportevent")
    elif k == 3:
        C.execute("SELECT * FROM store ORDER BY sportevent")
    elif k == 4:
        C.execute("SELECT * FROM store ORDER BY username")

    results = C.fetchall()
    for row in results:
        print(row)
database()
