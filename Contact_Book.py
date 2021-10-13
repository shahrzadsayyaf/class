import mysql.connector as cd
mydb=cd.conncet(host="localhost",user="root",passwd="tiger",database="contact")
mycursor=mydb.cursor()
def add_contacts():
    L=[]
    mobile_no=input("Enter Moobile number(10 digits):")
    L.append(mobile_no)
    name=input("Enter the Name:")
    L.append(name)
    address=input("Enter address:")
    L.append(address)
    email=input("Enter the email:")
    L.append(email)
    cont=(L)
    sql="inser intp contact_book(mobile_no,address,email)values(%s,%s,%s,%s)"
    mycursor.execute(sql,cont)
    mydb.commit()
def view_contact():
    print("Selelct the search criteria:")
    print("1.Mobile_no")
    print("2.Name")
    print("3.Address")
    print("4.Email")
    print("5.All contacts")
    ch=int(input("Enter your choice:"))
    if(ch==1):
        s=input("Enter mobile Number:")
        rl=(s,)
        sql="select * from contact_book where mobile_no=%s"
        mycursor.execute(sql,rl)
    elif(ch==2):
        nm=input("Enter Name:")
        rl=(nm,)
        sql="select * from contact_book where name='%s';"%nm
        mycursor.execute(sql)
    elif(ch==3):
        s=input("Enter address:")
        rl=(s,)
        sql="select * from contact_book where email=%s;"
        mycursor.execute(sql.rl)
    elif(ch==5):
        sql="select*from contact_book;"
        mycursor.execute(sql)
        res=mycursor.fetchall()
        print("The contact details are as follows:")
        print("mobile_no, name, address, email)")
    for x in res:
        print(x)
def del_contact():
    name=input("Enter the name to be deleted:")
    rl=(name,)
    sql="delete from contact_book where name=%s"
    mycursor.execute(sql,rl)
    mydv.commit()
def Main_Menu():
    print("Enter1: TO ADD NEW CONTACT")
    print("ENTER2: TO VIEW CONTACT")
    print("ENTER3: TO SEARCH CONCTACT")
    print("ENTER4: TO DELETE CONTACT")
    try:
        userInput=int(input("Please Select An Above Option:"))
    except ValueError:
        exit("\nHy!Thats Not A Number")
    else:
        print("\n")
        if(userInput==1):
            add_contact()
        elif(userInput==2):
            view_contact()
        elif(userInput==3):
            search_contact()
        elif(userInput==4):
            del_contact()
        else:
            print("Enter correct choice")
  Main_Menu()
ch=input("\nwant to continue Y/N:")
while(ch=='Y'or ch=='y'):
    Main_Menu
Main_Menu()
ch=input("\nwant to run again Y/N:")
