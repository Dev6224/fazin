import os
import csv

def buy(iddsv, x):
    l = []
    with open("sports.csv","r") as f:
        pr = csv.reader(f)
        l = list(pr)
    for i in l:
        if i[0] == iddsv:
            i[2] = y
            i[2] = y-x
    with open("sports.csv", "w") as k :
        p = csv.writer(k)
        p.writerow(l)
        
        



def additem():
    print("Add a new item")
    print("================")
    f=open('sports.csv','a',newline='\r\n')
    s=csv.writer(f)
    itemno=int(input('Enter sportid='))
    sportitem=input('Enter sport item=')
    quantity=float(input('Enter no of items='))
    price=float(input("enter price"))
    rec=[itemno,sportitem,quantity,price]
    s.writerow(rec)
    f.close()
    print(""""++++++++++++++++++++++++SUCCESSFULLY ADDED++++++++++++++++++++++++""")
    input("Press any key to continue..")

def modifyitem():
    print("Modify a Record")
    print("================")
    f=open('sports.csv','r',newline='\r\n') 
    f1=open('temp.csv','w',newline='\r\n')
    f1=open('temp.csv','a',newline='\r\n')
    r=input('Enter itemno you want to modify')
    s=csv.reader(f)
    s1=csv.writer(f1)
    for rec in s:
        if rec[0]==r:
            print("itemno=",rec[0])
            print("sportitem=",rec[1])
            print("quanitity=",rec[2])
            print("price=",rec[3])
            c1=input("Do you want to modify the sport item(y/n)")
            if c1=='y' or c1=='Y':
                sportitem=input('Enter new name=')
            c2=input("Do you want to modify the quantity(y/n)")
            if c2=='y' or choice=='Y':
                quanitity=float(input('Enter quanitity='))
            c3=input("Do you want to modify the price(y/n)")
            if c3=='y' or choice=='Y':
                price=float(input("enter price"))
                rec=[itemno,sportitem,quantity,price]
                s1.writerow(rec)
                print("Record Modified")
            else:
                s1.writerow(rec)
        else:
            s1.writerow(rec)
    f.close()   
    f1.close()
    os.remove("sports.csv")
    os.rename("temp.csv","sports.csv")
    
    input("Press any key to continue..")

def deleteitem():
    f=open('sports.csv','r',newline='\r\n') 
    f1=open('temp.csv','w',newline='\r\n')
    f1=open('temp.csv','a',newline='\r\n')
    r=input('Enter itemno you want to delete')
    s=csv.reader(f)
    s1=csv.writer(f1)
    for rec in s:
        if rec[0]==r:
            print("itemno=",rec[0])
            print("sportitem=",rec[1])
            print("quanitity=",rec[2])
            print("price=",rec[3])
            choice=input("Do you want to delete this record(y/n)")
            if choice=='y' or choice=='Y':
                pass
                print("Record Deleted")
            else:
                s1.writerow(rec)
        else:
            s1.writerow(rec)
    f.close()
    f1.close()
    os.remove("sports.csv")
    os.rename("temp.csv","sports.csv")
    
    input("Press any key to continue..")


def viewall():
    print("List of All Records")
    print("===================")
    f=open('sports.csv','r',newline='\r\n')  
    s=csv.reader(f)
    i=1
    for rec in s:
        print(rec[0],end="\t\t")
        print(rec[1],end="\t\t")
        print(rec[2],end="\t\t")
        print(rec[3])
        i+=1
    f.close()
    input("Press any key to continue..")
