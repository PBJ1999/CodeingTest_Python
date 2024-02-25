a = int(input("enter a 'n'>>"))

b = list(map(int, input("enter a num size of {} >>".format(a)).split()))

print("sum: {}".format(sum(b)))
print("avg: {}".format(sum(b)/len(b)))
print("max: {}".format(max(b)))
print("min: {}".format(min(b)))
