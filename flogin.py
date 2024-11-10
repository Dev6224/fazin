# Simple User System with Login and Sign Up

with open("users.csv", "wb") as f:
            g = ["test","hello","role"]
            m = csv.writer(f)
            m.writerow(g)
def basic():
        with open("users.csv", "rb") as f:
            u = csv.reader(f)
            l = list(u)
            return(l)
    

def sign_up(username, password, role):
    users = basic()
    """Sign up a new user with username, password, and role"""
    if username in users:
        print("Username already taken.")
                sign_up(username,password,role)
    else:
        users[username] = {'password': password, 'role': role}
        print(f"User '{username}' registered as {role}.")

def login(username, password): 
    users = basic()
    if username in users and users[username]['password'] == password:
       return(role)
    else:
        print("Invalid username or password.")
