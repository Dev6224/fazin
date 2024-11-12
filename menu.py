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
      print("1.Sales History \n 2.Review System \n 3.User system
    
  
  


    
  
  
