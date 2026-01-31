#task 5.3


def maxsep(n1,n2):

    while n2 != 0:
        n1, n2 = n2, n1 % n2

    return n1

def maxofthree(data):

    if data[0] > data [1]:
        data[1] = data[0]
    if data [1] > data [2]:
        data [2] = data [1]

    return max(data[2])

def vis_year(year):
    if year % 400 == 0:
        print("Високосный")
    elif year % 4 == 0:
        if year % 100 != 0:
            print("Високосный")
    else:
        print("Не високосный")