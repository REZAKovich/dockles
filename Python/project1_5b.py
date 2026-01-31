#task1===========================================================================#

# def nonechecker(data):
#     while True:
#         try:
#             data.remove('None')
#         except ValueError:
#             break

# def avgtemp(data):
#     nonechecker(data)
#     return sum(data)/len(data)

# nums = list(map(int, input("Введите числа через пробел: ").split()))

# print(avgtemp(nums))

#task2===========================================================================#

# def listsort(*args):

#     overzero =[]
#     lowerzero = []

#     for i in args:
#         if i<0:
#             lowerzero.append(i)
#         else:
#             overzero.append(i)

#     lowerzero.sort(reverse=True)
#     overzero.sort()

#     return overzero, lowerzero

#task3===========================================================================#

# def degclassic(a,b):
#     return a**b

# def degrec(a,b):
#     if b == 0:
#         return 1
#     return a * degrec(a,b-1)

# print(degclassic(2,3))

# print(degrec(2,5))