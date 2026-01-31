#from statistics import mean

print('Введите значения продаж (для конца списка введите EOF)')

data = []
cnt = 1
avg = 0
while True:
    selldata = input(str(cnt) + ': ')
    if selldata == 'EOF' or selldata == 'eof':
        break
    data.append(int(selldata))
    cnt+=1

for i in data:
    avg += i
avg = avg/len(data)

print('Среднее значение за все периоды: ' + str(avg) + '\n')

#print('Среднее значение за все периоды: ' + str(mean(data)) + '\n')

data.sort()

for i in data:
    print(i)