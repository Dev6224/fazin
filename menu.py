print("Welcome to the sports store:")
print("perhaps you might want to login")
a = input("Enter the username")
b = input("Enter the password")
m = login(a,b)
if m == None:
  print("Sign up or exit")
  x = input()[0].lower()
  if x == "s":
    print("Enter the role employee(e) or user(u)")
    y = input()[0].lower()
    if y == "e":
      sign_up(a,b,"employee")
      print("logging in")
      m = login(a,b)
    if y == "u":
      sign_up(a,b,"user")
      print("Logging in")
      m = login(a,b)
while True:
    if m[2] == "user":
      print("1 for browsing, 2 for buying 3 for exiting")
      r == int(input())
      if r == 1:
        listofitems()
        print("Enter anything to continue")
        w = input()
        continue
      elif r == 2:
        buyt()
        continue
      elif r == 3:
        print("Exiting")
        break
    if m[2]  == "employee":
      print("1.Sales History \n 2.Review System \n 3.User system")
				z = int(input())
				if z == 1:
					print("\n==== Sports Store Management Menu ====")
        print("1. Create Database and Table")
        print("2. Add a New Purchase")
        print("3. Delete All Records")
        print("4. List All Items")
        print("5. Show Last Record")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            database()
            tablesport()
            print("Database and table setup completed.")
        elif choice == '2':
            buyt()
        elif choice == '3':
            deleter()
        elif choice == '4':
            listofitems()
        elif choice == '5':
            get_last_record()
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
				elif z == 2:
					

   	
						
    
  
  


    
  
  
