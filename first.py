# THE MASTER LOOP: This keeps the whole app running until we use 'break'
while True:
    print("\n--- RTO LICENSE PORTAL ---")

    # 1. Collecting User Details (Inside the loop so it asks again if needed!)
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    ph_no = input("Enter your phone number: ")
    addhar_no = input("Enter your addhar number: ")

    # Combining names
    name = last_name + " " + first_name
    age = int(input("Enter you age: "))
    Amount = 4500

    # 2. UI Display
    print("\nCheck given details")
    print("___" * 10)
    print(f"Name: {name}")
    print(f"Phone: {ph_no}")
    print(f"Aadhar: {addhar_no}")
    print(f"Age: {age}")
    print("___" * 10)

    given_details = input(
        "If given details are correct, enter 'yes' or 'no': ").lower()

    # 3. THE CORE LOGIC
    # We use 'if' here, not 'while', because the MASTER loop is handling the repetition
    if given_details == "yes":

        if age >= 18:
            print("\nYou are eligible of driving licence")
            print("The Amount need to pay for licence is Rs. {}".format(Amount))

            pay = int(input("Please enter amount to pay: Rs. "))

            if pay == Amount:
                print("Thank you, please collect your receipt.")
                break  # <-- PROCESS COMPLETE. Stops the Master Loop.

            elif pay > Amount:
                change = pay - Amount
                print(f"Please collect your change: Rs. {change}")
                break  # <-- PROCESS COMPLETE. Stops the Master Loop.

            else:
                print("Insufficient payment. Process stopped.")
                break  # <-- PAYMENT FAILED. Stops the Master Loop.

        else:
            print("\nYou are not eligible for a license because you are under 18.")
            break  # <-- NOT ELIGIBLE. Stops the Master Loop.

    # 4. HANDLING MISTAKES (The power of 'continue')
    elif given_details == "no":
        print("\nRestarting so you can fix your details...")
        continue  # <-- Jumps to line 2, asking for first_name again!

    else:
        print("\nInvalid typing. Please just type 'yes' or 'no'. Restarting...")
        continue  # <-- Jumps to line 2
