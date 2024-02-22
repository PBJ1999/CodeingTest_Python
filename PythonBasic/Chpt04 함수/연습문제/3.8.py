inputStr = input(">>")
inputStrList = list(inputStr.split(','))

a1 = []

for i in inputStrList:
    a1.append(int(i))

print("입력된 정수의 리스트: {}".format(list(a1)))
a1.sort()

print(a1, end=' ')








