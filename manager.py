import os
def password_encryption():
    try:  
        with open("1.txt","r") as f:
            user=input("Enter the app whom for you want the password: ")
            data=f.readlines()
            i=0
            while(i<len(data)):
                a=data[i].split(':')
                if a[0]==user:
                    return a[1]
                i+=1
        return "no such app. "
    except FileNotFoundError:
        return "FIRST SAVE THE PASSWORD FOR A APP AND THEN ONLY YOU CAN SEE."
def update():
    app_name=input("Enter the app name: ")
    old_password=input("Enter the  old password: ")
    info=app_name+':'+old_password+'\n'
    with open("1.txt",'r') as f:
        n=f.readlines()
    if info not in n:
        return "No such app or password is present."
    else:
        for i in n:
            info=i.split(':')
            if info[0]==app_name:
                if info[1]==old_password+'\n':
                    n.remove(f"{app_name}:{old_password}\n")
                    n.append(f"{app_name}:{input("Enter the new password: ")}\n")
                    
                else:
                    return "Password is not correct. Enter 3 again to try again."
                with open("1.txt","w") as f:
                    f.writelines(n)
                    return "Password is set."
        

def password_decryption():
    a=[input("Enter the app whom you want to save the password for: \n")
    ,input("Enter the password: ")]
    # a[1]=storing_key.encrypt(a[1].encode())
    file_name=f"1.txt"
    if os.path.exists(file_name):
        with open(file_name,"a") as f:
            f.writelines(f"{a[0]}:{a[1]}\n")
            return "Your passwd has been saved."
    else:
        with open(file_name,"w") as f:
            f.writelines(f"{a[0]}:{a[1]}\n")
            return "Your passwd has been saved."   

def delete():
    with open("1.txt",'r') as f:
        n=f.readlines()
    if len(n)==0:
        return "NO App and password is present."
    app=input("Enter the app name: ")
    password=input("Enter the password: ")
    info=app+':'+password+'\n'
    if info in n:
        n.remove(info)
        with open("1.txt","w") as f:
            f.writelines(n)
            return "APP AND PASSWORD IS DELETED."
    
    else:
        return ("NO SUCH APP OR PASSWORD IS PRESENT . ENTER 3 TO TRY AGAIN.")   
    


if os.path.exists('master_password.txt'):
    master_key=input("Enter the master password: ")
    with open("master_password.txt","r") as f:
        data=f.read()
        if data==master_key:
            print("""Press the number for which you want the operation to be done(1,2,3,4).(q for exit)
      Press 1 for saving the password,2 for seeing the passwd""")
            while True:
                opr=input("Enter the opr you want to perform: ")
                if opr=='1':
                    print(password_decryption())
                if opr=='2':
                    print(password_encryption())
                if opr=='3':
                    print(update())
                if opr=='4':
                    print(delete())
        else:
            print("Enter the correct master password or contact to 121 for changing the password.")
else:
    print("""Welcome to the app and it's your first time you are visiting the app, so
          enter the master passowrd""")
    master_key=input("Enter the master password: ")
    with open("master_password.txt","w") as f:
        f.write(master_key)
    print("""Press the number for which you want the operation to be done(1,2,3,4).(q for exit)
      Press 1 for saving the password,2 for seeing the passwd""")
    while True:
        opr=input("Enter the opr you want to perform: ")
        if opr=='1':
            print(password_decryption())
        if opr=='2':
            print(password_encryption())
        if opr=='3':
            print(update())
        if opr=='4':
            print(delete())
        # else:
        #     print("Enter the correct master password or contact to 121 for changing the password.")


        
        
                
                
                

