"""This program is for zamoto"""
Total_amount = 0
cart = 0
discount = 0
while True:
    print("\t---Menu---")
    print("1.Biriyani-RS.120₹")
    print("2.Egg Rice-Rs.60₹")
    print("3.Mutton Biriyani-Rs.240₹")
    print("4.chilli chicken-RS.220₹")
    print("5.Dosa-Rs.30₹")
    print("6.Idli-RS.25₹")
    print("7.Check out and payment")
    print("8.Exit")
    user_choice = int(input("Please select the Item:"))
    if user_choice == 1:
        Qantity = int(input("enter the no.of qantity:"))
        print("Your item is added to the cart")
        cart = cart+Qantity
        Total_amount = Total_amount+Qantity*120
        print("The total items you added to the cart -{}".format(cart))
        print("Total Amount {}".format(Total_amount))
    elif user_choice == 2:
        Qantity = int(input("enter the no.of qantity:"))
        print("Your item is added to the cart")
        cart = cart+Qantity
        Total_amount = Total_amount+Qantity*60
        print("The total items you added to the cart- {}".format(cart))
        print("Total Amount {}".format(Total_amount))
    elif user_choice == 3:
        Qantity = int(input("enter the no.of qantity:"))
        print("Your item is added to the cart")
        cart = cart+Qantity
        Total_amount = Total_amount+Qantity*240
        print("The total items you added to the cart- {}".format(cart))
        print("Total Amount {}".format(Total_amount))
    elif user_choice == 4:
        Qantity = int(input("enter the no.of qantity:"))
        print("Your item is added to the cart")
        cart = cart+Qantity
        Total_amount = Total_amount+Qantity*220
        print("The total items you added to the cart- {}".format(cart))
        print("Total Amount {}".format(Total_amount))
    elif user_choice == 5:
        Qantity = int(input("enter the no.of qantity:"))
        print("Your item is added to the cart")
        cart = cart+Qantity
        Total_amount = Total_amount+Qantity*30
        print("The total items you added to the cart- {}".format(cart))
        print("Total Amount {}".format(Total_amount))
    elif user_choice == 6:
        Qantity = int(input("enter the no.of qantity:"))
        print("Your item is added to the cart")
        cart = cart+Qantity
        Total_amount = Total_amount+Qantity*25
        print("The total items you added to the cart- {}".format(cart))
        print("Total Amount {}".format(Total_amount))
    if Total_amount > 3000:
        discount = Total_amount*30/100
        print("The discount is applicible for your order {}".format(discount))
        Total_amount = Total_amount-discount
    elif Total_amount > 6000:
        discount = Total_amount*60/100
        print("The discount is applicible for your order {}".format(discount))
        Total_amount = Total_amount-discount
    elif Total_amount > 10000:
        discount = Total_amount*100/100
        print("The discount is applicible for your order {}".format(discount))
        Total_amount = Total_amount-discount
    elif user_choice == 7:
        print("Total Amount you need to pay '{}'".format(Total_amount))
        payment = int(input("please enter the amount:"))
    if payment >= Total_amount:
        print("Your order is conformed please wait for 20min😊")
        change = Total_amount-discount
        print("please collect the change {}".format(change))
        print("Thank for visiting😊")
        break
else:
    print("Insufficient amount. Please try paying again.")
