username1='vinay'
password1='9381062216'
username=input("enter username")
password=input("enter password")
if username==username1 and password==password1:
    print("you entered correct")
else:
    print("This is your first attempt")
    username=input("enter username")
    password=input("enter password")
    if username==username1 and password==password1:
        print("password is correct")
    else:
        print("This is your second attempt")
        username=input("enter username")
        password=input("enter password")
        if username==username1 and password==password1:
            print("correct")
        else:
            print("This is your last attempt")
            username=input("enter username")
            password=input("enter password")
            if username==username1 and password==password1:
                print("correct")
            else:
                print("attemts are over")
        
        
