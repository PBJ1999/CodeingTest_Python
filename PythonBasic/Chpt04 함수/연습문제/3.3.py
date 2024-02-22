def mean3(a,b,c):
    return (a+b+c) / 3

def max3(a,b,c):
    print(max(a,b,c))

def min3(a,b,c):
    print(min(a,b,c))


a,b,c = map(int, input().split())

print(mean3(a,b,c))

max3(a,b,c)
min3(a,b,c)
