inData = input("Введите Ваши имя и фамилию в формате ИМЯ ФАМИЛИЯ: ")

indSep = inData.find(" ")

fstnamestr = inData[:indSep]
fstnamestr = fstnamestr.title()

scndnamestr = inData[indSep+1:]
scndnamestr = scndnamestr.title()
 
fullName = fstnamestr + " " + scndnamestr

userLogin = scndnamestr[0:4] + fstnamestr[0]

print(fullName + ": " + userLogin)