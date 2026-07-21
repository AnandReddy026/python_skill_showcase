n = int(input("enter a number:"))
k = 0
i = 0
for i in range(1, n+1):
    if n % i == 0:
        k += 1
if k == 2:
    print("it is a prime")
else:
    print("it is not prime")
