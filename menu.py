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
      print("1.Sales History \n 2.Review System \n 3.Supplier system \n 4. Items 5. Exit ")
				z = int(input())
				if z == 1:
					print("\n==== Sports Store Management Menu ====")
        print("1. Add a New Purchase")
        print("2. Delete All Records")
        print("3. List All Items")
        print("4. Show Last Record")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

       
        iff choice == '1':
            buyt()
        elif choice == '2':
            deleter()
        elif choice == '3':
            listofitems()
        elif choice == '4':
            get_last_record()
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
				elif z == 2:
					while True:
        	print("\n==== Bills and Reviews Management Menu ====")
        	print("1. Add a Bill and Review")
        	print("2. Display All Bills and Reviews")
        	print("3. Exit")
        	choice = input("Enter your choice (1-3): ")

        	if choice == '1':
            	add_bill_review()
        	elif choice == '2':
            	display_bills_reviews()
        	elif choice == '3':
            	print("Exiting the program.")
            	break
        	else:
            	print("Invalid choice. Please try again.")
					elif z == 3:
							supplier_menu()
					elif z ==4:
								while True:
        		print("\n==== Sports Inventory Management Menu ====")
        		print("1. Add a New Item")
        		print("2. Modify an Item")
        		print("3. Delete an Item")
        		print("4. View All Items")
        		print("5. Buy an Item")
        		print("6. Exit")
        		choice = input("Enter your choice (1-6): ")

        		if choice == '1':
            		additem()
        		elif choice == '2':
            		modifyitem()
        		elif choice == '3':
            		deleteitem()
        		elif choice == '4':
            		viewall()
        		elif choice == '5':
            		item_id = input("Enter item ID to buy: ")
            		quantity = int(input("Enter quantity to buy: "))
            		buy(item_id, quantity)
        		elif choice == '6':
            		print("Exiting the program.")
            		break
        		else:
            		print("Invalid choice. Please try again.")
					elif z ==5:
								print("Exiting")
								break


   	
						
    
  
  


    
  
  
