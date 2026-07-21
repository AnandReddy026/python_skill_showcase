"""This program is for password checking"""
chances = 4
while True:
    Password_from_user = int(input("Please Enter the '4' digit Password:"))
    password = 3015
    if Password_from_user == password:
        print("Phone was Unlocked")
        break
    else:
        print("Invalid password,please Try again")
        chances = chances-1
        print("you have only {}".format(chances))
    if chances == 0:
        print("The phone was locked wait for 30 seconds")
        break
