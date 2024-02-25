a1 = list(map(int, input().split()))

sum_num = sum(a1)
max_num = max(a1)
min_num = min(a1)

print("sum = {}".format(sum_num))
print("avg = {}".format(sum_num/len(a1)))
print("max = {}".format(max_num))
print("min = {}".format(min_num))