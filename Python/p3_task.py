import calendar

#task 3.1

data = []

for i in range(0,3):
    data.append(input("Enter number: "))

if data[0] > data [1]:
    data[1] = data[0]
if data [1] > data [2]:
    data [2] = data [1]

print("Highest number is: " + str(data[2]))

#task 3.2

year = 1412

#if+else
if year % 4 == 0:
    if year % 100 != 0:
        print("Високосный")
else:
    print("Не високосный")


#elif
if year % 400 == 0:
    print("Високосный")
elif year % 4 == 0:
    if year % 100 != 0:
        print("Високосный")
else:
    print("Не високосный")
    
#if+calendar
if calendar.isleap(year): print("Високосный")