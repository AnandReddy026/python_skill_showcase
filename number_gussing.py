"""This program is for gussing the Number"""
scerect_number = 26
attempet = 0
while True:
    User_number = int(input("Enter the number for gussing:"))
    attempet = attempet+1
    if scerect_number == User_number:
        print("yahoo🎉,You entered the correct number {}".format(scerect_number))
        break
    elif User_number > scerect_number:
        print("You are near to the number,please enter low number")
    else:
        print("you entered the higher number")
