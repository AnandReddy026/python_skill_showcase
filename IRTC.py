available_seats = 20  # (Train lo unna total seats)
ticket_price = 500
wallet = 5000
my_tickets = 0
while True:
    print("--Welcome to IRTC--")
    print("1. Check Status (Seats & Balance)")
    print("2. Book Tickets")
    print("3. Cancel Tickets")
    print("4. Exit")
    choice = int(input("Please enter the options for your process:"))
    match choice:
        case 1:
            print("available seats are {}".format(available_seats))
            print("Total amount in your wallet is {}".format(wallet))
        case 2:
            qty = int(input("How many tickets do you want? "))
            if qty <= available_seats:
                total_cost = qty * ticket_price
                if total_cost <= wallet:
                    wallet = wallet - total_cost
                    available_seats = available_seats - qty
                    my_tickets = my_tickets + qty
                    print("Booking Successful! 🎉")
                else:
                    print("Insufficient Balance in Wallet!")
            else:
                print(f"Sorry, only {available_seats} seats are available!")
        case 3:
            cancel_qty = int(input("How many tickets to cancel? "))
            if qty <= available_seats:
                total_cost = qty * ticket_price
                if cancel_qty <= my_tickets:
                    refund = cancel_qty * ticket_price
                    wallet = wallet + refund
                    available_seats = available_seats + cancel_qty
                    my_tickets = my_tickets - cancel_qty
                    print(
                        "Cancellation Successful! Rs. {refund} refunded to your wallet.")
                else:
                    print("You don't have that many tickets to cancel!")
        case 4:
            print("Thank you for using Mini IRCTC! Happy Journey!")
            break
else:
    Print("Invalid Option. Please try again.")
