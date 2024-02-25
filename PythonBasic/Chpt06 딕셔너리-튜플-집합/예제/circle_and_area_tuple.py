def a_and_c(r):
    a1 = 3.14 * r ** 2
    c1 = 2 * 3.14 ** 2
    return a1, c1

r = 4

a,c = a_and_c(r) # unpacking

print(a,c)