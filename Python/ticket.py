ticket = list(input("Enter number of ticker (6 ch.): "))

ticket = list(map(int,ticket))

num1 = sum(ticket[:3])
num2 = sum(ticket[3:])

if num1 == num2:
    print("Lucky ticket!")
else:
    print("Not today...")