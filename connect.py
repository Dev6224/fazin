def connect():
        import mysql.connector
        DB=mysql.connector.connect(host="localhost",user="root",password="tiger")
        C=DB.cursor()
def database():
        q="create database sportsstore"
        C.execute(q)
        qq="use sportsstore"
        C.execute(qq)

def tablesport():
        w= "create table store(regno int primary key, username varchar(15),  item_no int  , sportevent varchar(15) , quantity int , price int)"
        C.execute(w)
        
def buyt():
        item_no=int(input("enter item if"))
        sportitem=str(input("Enter sport item: "))
        sportevent=str(input("sport event:"))
        quantity=int(input("Enter quantity:"))
        brand=str(input("Enter brand name:"))
        price=int(input("Enter the price:"))
        C.execute("INSERT INTO store({},'{}','{}',{},'{}',{})".format(sportitem,sportevent,quantity,brand,price))
        DB.commit()
        print("""++++++++++++++++++++++++SUCCESSFULLY ADDED++++++++++++++++++++++++""")
def delete():
        bb=input("Are you sure(Y/N):").upper()
        if bb=="Y":
                C.execute("delete from sell_rec")
        DB.commit()
def listofitems():
        print("1-item no , 2-sport item , 3-sportevent , 4-brand")
        k=input("want to see products order by(1,2,3,4)")
        if k==1:
                C.execute("select * from store order by item_no")
        elif k==2:
                C.execute("select * from store order by sportitem")
        elif k==3:
                C.execute("select * from store order by sportevent")
        elif k==4:
                C.execute("select * from store order by brand")

def mgmt( ):
        print(" 1. Add New Product")
        print(" 2. List Product")
        print(" 3. Update Product")
        print(" 4. Delete Product")
        print(" 5. Back (Main Menu)")
        p=int (input("Enter Your Choice :"))
        if p==1:
                ADD()
        if p==2:
                listofitems()
        if p==3:
                update_product()
        if p==4:
                delete()
        if p== 5 :
            pass

mgmt()
