a = [10,20,30,50,60]
for i in range(len(a)):
    min_num = a[0]
    if min_num > a[i]:
        min_num = a[i]

print("{}".format(min_num))