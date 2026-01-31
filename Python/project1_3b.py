import random
import Random_names

#task1

# randlist = []
# statuslist = []

# alertHigh = 80
# alertMedium = 50


# for i in range(99):
#     randlist.append(random.randrange(1,100))

# for i in randlist:
#     if i < alertMedium:
#         statuslist.append('Low')
#     elif alertMedium <= i < alertHigh:
#         statuslist.append('Medium')
#     else:
#         statuslist.append('High')

# for i in range(0,99):
#     print("#" + str(i) + "|" + str(randlist[i]) + "|" + statuslist[i])

#task2

# nameslist = []
# AMfchar = []
# otherfchar = []

# for i in range(100):
#     nameslist.append(Random_names.names.get_full_name())
    
# for i in nameslist:
#     if i[0] == 'A' or i[0] == 'M':
#         AMfchar.append(i)
#     else:
#         otherfchar.append(i)

# print(str(nameslist) + "\n")
# print(str(AMfchar) + "\n")
# print(str(otherfchar) + "\n")

#task3

data = []
outword = []

while True:

    tempdata = input("Введите слово:")
    if tempdata == "":
        break
    data.append(tempdata)
    

for i in data:
    outword.append(str(i[0]))

print(''.join(outword))