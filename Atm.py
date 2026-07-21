while True:
    print("\n---ATM MACHINE---")
    print("---WELCOME---")
    print("Please insert your card for processes")
    Acc_no = int(input("please enter your account number:"))
    ph_n0 = int(input("please enter your phone number:"))
    correct_pin = 6304
    acc_no = 454838394933
    Ph_no = 5839384834
    Balance = 20000
    user_pin = int(input())
    if acc_no == Acc_no:
        if ph_n0 == Ph_no:
            if correct_pin == user_pin:
                Amount = int(input("please enter the Amount:"))
            elif Amount <= Balance:
                print("please collect The Amount {}".format(Amount))
                Balance = Balance-Amount
                print("The Remaning Balance is: RS.{}".format(Balance))
                break
            else:
                print("Please enter the Correct pin")
                print("you entered the pin is {}".format(user_pin))
                continue
        else:
            print("please Check the Phone number")

    else:
        print("Please Enter the correct Account number")
