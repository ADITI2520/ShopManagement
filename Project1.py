import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",password="12345",db="mydata")
print(con)
mycursor=con.cursor()

#INSERT PRODUCT CODE

def Insert():
    
    Pid=int(input("Enter Product ID: "))
    Pname=input("Enter Product Name: ")
    Pcategory=input("Enter Product Category: ")
    Psubcategory=input("Enter Product Sub Category: ")
    Price=int(input("Enter Product Price: "))

    sql="insert into product values(%s,%s,%s,%s,%s)"
    val=(Pid,Pname,Pcategory,Psubcategory,Price)
    mycursor.execute(sql,val)
    print("Products Added Sucessfully!!")
    con.commit()

#DISPLAY PRODUCT CODE

def Display():

    
    sql="select * from product"
    mycursor.execute(sql)
    data=mycursor.fetchall()
    print("Displaying All Products")
    for r in data:
        for c in r:
            print(c,end=" | ")
        print()
    
#DISPLAY BY PRODUCT ID CODE

def DisplayByID():
    while True:
        Pid=int(input("Enter Product Id To Be Searched if not the enter 0: " ))
        sql="select * from Product where Pid=%s"
        val=(Pid,)
        mycursor.execute(sql,val)
        data=mycursor.fetchall()
        for r in data:
            for c in r:
                print(c,end=" | ")
            print()

        if Pid==0:
            break

        else:
            flag=0
            for i in data:
                if i[0]==Pid:
                    flag=1
                    break
            if flag==0:
                print("Please Entry The Proper Product Id To Be Searched")
                print("")
            else:
                break
            
            
        


#DELETE PRODUCT CODE


def Delete():
        
        Pid=int(input("Enter Product Id To BE Deleted: "))
        sql="select * from product where Pid=%s"
        val=(Pid,)
        mycursor.execute(sql,val)
        data=mycursor.fetchall()
        for r in data:
            for c in r:
                print(c,end=" | ")
            print()

        
            
        if len(data)!=0:
            sql="delete from Product where Pid=%s"
            val=(Pid,)
            mycursor.execute(sql,val)
            data=mycursor.fetchall()
            print("Product Deleted Sucessfully!!")
            con.commit()
        else:
            print("No Such Product ID To Be Deleted")
        

                              
        

#EDIT PRODUCT i.e UPDATE PRODUCT

def Edit():
    
    Pid=int(input("Enter Product Id To Be Edited: "))
    sql="select * from Product where Pid=%s"
    val=(Pid,)
    mycursor.execute(sql,val)
    data=mycursor.fetchall()
    for r in data:
        for c in r:
            print(c,end=" | ")
        print()

    if len(data)!=0:
        Pname=input("Enter Product Name To Be Edited Else Leave Empty: ")
        if Pname=="":
             Pname=data[0][1]
                
        Pcategory=input("Enter Product Category To Be Edited Else LEave Empty: ")
        if Pcategory=="":
            Pcategory=data[0][2]
                
        Psubcategory=input("Enter Product Subcategory To Be Edited else Leave Empty: ")
        if Psubcategory=="":
            Psubcategory=data[0][3]
                
        Price=int(input("Enter PRoduct Price To Be Edited Else LEave Empty: "))
        if Price=="":
            Price=data[0][4]
        else:
            Price=int(Price)

        sql="update Product set Pname=%s,Pcategory=%s,Psubcategor=%s,Price=%s where Pid=%s"
        val=(Pname,Pcategory,Psubcategory,Price,Pid)
        mycursor.execute(sql,val)
        print("Product Edited Sucessfully!!")
        con.commit()
        
    elif len(data)!=Pid:
        print("Their Is No Such Id To BE Edited Please Enter Valid Id")
           
        

#SEARCH BY NAME PRODUCT CODE

Pname=[]
def SearchByName():
            Pname=input("Enter Product Name To Be Searched: ")
            sql="select * from Product where Pname like '{0}%'".format(Pname)
            mycursor.execute(sql)
            data=mycursor.fetchall()
            for r in data:
                for c in r:
                    print(c,end=" | ")
                print()
                
            if len(data)!=0:
                sql="select * from Product where Pname like '{0}%'".format(Pname)
                mycursor.execute(sql)
                data=mycursor.fetchall()
                for r in data:
                    for c in r:
                        print(c,end=" | ")
                    print()
            else:
                print("Not Found")
                
                
#-------------------------------------------------------
#CUSTOMER ADD PRODUCT CODE


carts=[]
prices=[]
total=[]
qty=[]
name=[]
discount=[]
def CustomerAdd():
    
    sql="select * from Product"
    mycursor.execute(sql)
    data1=mycursor.fetchall()
    for r in data1:
        for c in r:
            print(c,end=" | ")
        print()
    
    while True:
        Pid=int(input("Enter Product Id To Be Added In Cart and(Enter 0 to stop): "))

        if Pid==0:
            break

        else:
            flag=0
            for i in data1:
                if i[0]==Pid:
                    flag=1
                    break
            #print(flag)
            if flag==0:    
                raise RangeError("Please Entry Valid Id ")
        
            else:
            
                sql="select * from Product where Pid=%s"
                val=(Pid,)
                mycursor.execute(sql,val)
                data=mycursor.fetchall()
                carts.append(data[0][0])                
                q=int(input("Enter Quantity:"))
                qty.append(q)
                p=q*int(data[0][4])
                prices.append(p)
                name.append(data[0][1])
                    
        print()
        print("Added The Product To The Cart")   
        print("ProductId",carts,"\nPrice",prices)
        print()
    
        



def View():
   
        if len(carts)==0:
            raise EmptyErrorException("View cannot Be Empty")
            self.cart=self.cart
        
        else:
            print("This Is what In Your Cart: ")
            print("id  -  Name  -  Qty    \n\n")
            for i in range(0,len(prices)):
                print(carts[i]," -    ",name[i]," - ",qty[i]," ")
                #print(carts,prices)
            print()
        
    
    
    
def Remove():

    if len(carts)==0:
        raise EmptyException("There Is Nothing To Be Removed")
    else:
        
        print("This Is what In Your Cart: ")
        print("id  -  Name  -  Qty    \n\n")
        for i in range(0,len(prices)):
                print(carts[i]," -    ",name[i]," - ",qty[i]," ")
                #print(carts,prices)
        print()
        
        #print(carts,prices)
        print()
        remo=int(input("Enter Product ID To Be Removed From Cart: "))
        i=carts.index(remo)
        carts.remove(remo)
        prices.remove(prices[i])
        print("Product Removed Sucessfully!!")
        print()
        print("This Is what In Your Cart: ")
        print(carts,prices)
        print()


def Bill():
    
    sum=0
    for p in prices:
        sum+=int(p)
        
    d=(sum*10)/100
    discount=sum-d
        
    print("This is The Total Bill Of Your Product\n")
    print("")
    print("id  -  Name  -  Qty   -   Price \n\n")
    for i in range(0,len(prices)):
        print(carts[i]," -    ",name[i]," - ",qty[i]," - ",prices[i]," ")  

    #print(carts,prices)
    print("------------------------------------\n")
    print("This Is Your Total Purchase Bill             : ",sum)
    print("You Got A 10% Discount On Your Total Purchase: ",d)
    print("This Is Your Finall Amount             : ",discount)
    print()
    
#--------------------------LOGIN CODE OF CUSTOMER AND ADMIN--------------------------------------
    
def authAdmin():
    print("")
    print("Admin Login")
    print("")
    admin_login=input("Enter UserName: ")
    admin_pass=input("Enter PassWord: ")
    if admin_login=="admin":
        if admin_pass=="password":
            print("Successfully Login To Admin Page")
            print("")
        else:
            print()
            
    else:
        raise LogInException("LogIn Details Not Recognised Please Try Again")


Id=[]
customername=[]
Password=[]
data=[]

def custLogin():
    while True:
        print("")
        cust_login=int(input("1.Already Had An Account LogIn\n2.New User Registered\n3.Exist\n"))
        print("")
        
        if cust_login==1:
            try:            
                Customername=input("Enter Name: ")
                Password=input("Enter Password: ")
                sql="select * from Customerlogin where customername=%s and password=%s"
                val=(Customername,Password)
                mycursor.execute(sql,val)
                data=mycursor.fetchall()
                
                if len(data)!=0:
                    print("Successfully LogIn")
                    print("")
                    print("SHOP NOW!!!")
                    break
                else:
                    print("Username and password not match..!!")
            except:
                raise InvalidException("Not resgistered Before Please Register First")
                    
        
        elif cust_login==2:
            try:
                
                Id=int(input("Enter Id: "))
                Customername=input("Enter Your Name: ")
                Password=input("Enter A Password: ")
                sql="insert into customerlogin values(%s,%s,%s)"
                val=(Id,Customername,Password)
                mycursor.execute(sql,val)
                data=mycursor.fetchall()
                print("Registered")
                con.commit()
                
        
            except:
                raise IntegrityException("Already Registered With This Id Please Enter another ID")

        elif cust_login==3:
            print("Existing From LogIn Page")
            break
        

            
#exception

class EmptyErrorException(Exception):
    pass

class EmptyException(Exception):
    pass

class RangeError(Exception):
    pass

class LogInException(Exception):
    pass

class IntegrityException(Exception):
    pass

class InvalidException(Exception):
    pass


#WRAPPING IN WHILE LOOP

while True:
    print("Enter Choice: ")
    n1=int(input("1.Admin\n2.Customer\n3.Cancel\n"))
    print("")
    if n1==1:
        try:
            authAdmin()
        except LogInException as le:
            print(le)
            authAdmin()
       
        
        while True:
            n=int(input("1=>Add Product\n2=>Display Product\n3=>Display Product By ID\n4=>Delete Product\n5=>Edit PRoduct\n6=>Search Product By Name\n7=>Exist\n"))
            if n==1:
                Insert()
                print()
                
            elif n==2:
                Display()
                print()
                    

            elif n==3:
                    DisplayByID()
                    print()
                
            elif n==4:
                Delete()
                print()

            elif n==5:
                Edit()
                print()

            elif n==6:
                SearchByName()
                print()

            elif n==7:
                print("Existing Admin Page")
                break
       
    elif n1==2:
        print("You Are At Customer Page")
        try:
            custLogin()
        except IntegrityException as ie:
            print(ie)
            custLogin()
            
        print("Enter Choice")
        while True:
            n1=int(input("1.Add Product To Cart\n2.View Cart\n3.Remove Product From Cart\n4.Bill\n5.Exist\n"))
            if n1==1:
                try:
                    print("Displaying Product Now You Can Add Them In Cart")
                    CustomerAdd()
                    print()
                except RangeError as r:
                    print(r)
                    print()
            elif n1==2:
                try:
                    View()
                    print()
                except EmptyErrorException as e:
                    print(e)
                    print()

            elif n1==3:
                try:                    
                    Remove()
                    print()
                except EmptyException as ee:
                    print(ee)
                    print()

            elif n1==4:
                Bill()
                print()

            elif n1==5:
                print("Thank You!!!")
                print()
                break
    elif n1==3:
        print("Out Of The App")
        break


