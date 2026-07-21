# this program is for student purpose
Name = input("enter your name:").lower()
section = input("enter your section:").lower()
address = input("enter your address:")
ph_no = int(input("enter your phone number:"))
details = input("if your details are correct please enter yes or no:").lower()
if details == "yes":
    if section == "it":
        print("you need to went to 10th Room")
    else:
        print("you need to went to 11th room")
else:
    print("please recheck the details")
