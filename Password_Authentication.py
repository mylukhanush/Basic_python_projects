import getpass
database = {"aman.kharwal": "123456", "kharwal.aman": "654321"}
username = input("Enter Your Username : ")
password = input("Enter Your Password : ")
for i in database.keys():
    if username == i:
        while password != database.get(i):
            password = input("Enter Your Password Again : ")
        break

    elif username != i :
        print("wrong username")
        break

    else:
        # print("not verified")
        print("Verified")

