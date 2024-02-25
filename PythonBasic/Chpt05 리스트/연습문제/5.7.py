a = [10, 20, 30, 50, 60]
for i in range(len(a)):
    max_num = a[0]
    if max_num < a[i]:
        max_num = a[i]

print("{}".format(max_num))