import csv
import os
from datetime import datetime

filepath = r'F:\DevOps Курс\Python\csvexamples\filesheat.csv'
logpath = 'F:\\DevOps Курс\\Python\\csvexamples\\logfile.txt'
pathtocopy = 'F:\\DevOps Курс\\Python\\csvexamples\\'

#timestamp = datetime.now().strftime("%Y-%m-%d__%H:%M:%S")

filelist = []

#проверка файла на существование
def fileexistcheсker(filepath):
    if not os.path.exists(filepath):
        with open(logpath,'a', encoding='utf-8', newline='') as file:
            file.write('CopyError: file ' + filepath + ' not exist\n')
            return 1
    else: return 0

#логирование копировки файла
def copylogger(name,path,newpath):
    with open(logpath,'a', encoding='utf-8', newline='') as file:
        file.write('Created file - name: ' + name + ' - path: ' + path + ' - path copyfile: ' + newpath + '\n')
    

def copyfile(rownum:int):

    data = []

    copyfilename = datetime.now().strftime("%Y-%m-%d__%H-%M-%S") + '_' +"".join(str(filelist[rownum][0])+".txt")
    copyfilepath = str(pathtocopy +copyfilename)

    if fileexistcheсker(str(filelist[rownum][1])) == 1:
        print('Error: File not exist')
        return
    
    with open(str(filelist[rownum][1]), 'r', encoding='utf-8', newline='') as file:
        data = list(csv.reader(file))

    with open(copyfilepath,'w',encoding='utf-8', newline='') as file:
        for i in data:
            file.write(str(i))

    print('Copy file complite')
    copylogger(copyfilename, copyfilepath, copyfilepath)

#чтение списка файлов
with open(filepath,'r', encoding='utf-8', newline='') as file:
    filelist = list(csv.reader(file))

print('Filelist for copy: ')
for i in filelist:
    if filelist.index(i) == 0:
        print(str(''.join(i[0]) + '\t' + ''.join(i[1])))
        continue
    print(str(filelist.index(i)) + ': ' + ''.join(i[0]) + '\t' + ''.join(i[1]))
    
rownumber = int(input('Enter num of file from list (over 0): '))

copyfile(rownumber)