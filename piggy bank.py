"""" This program is for piggy bank for saving money for buying the shoes"""
print("---Welcome to piggy Bank---")
saved_money = 0
while True:
    Add = int(input("Enter money for saving:"))
    saved_money = saved_money+Add
    if saved_money >= 2000:
        print("The Total is {}".format(saved_money))
        print("The savings are reached for buying the shoes👍")
        print("Take the money and buy the shoes")
        break
    else:
        print("The savings in your bank {}".format(saved_money))
        print("Keep saving")
        continue
