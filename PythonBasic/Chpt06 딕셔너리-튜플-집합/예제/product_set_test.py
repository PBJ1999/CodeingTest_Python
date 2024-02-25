def product_set(a, b):
    r = set()
    for i in a:
        for j in b:
            r = r | {(i,j)}
    return r

a = {1,2,3,4,5,6}

a1 = product_set(a,a)
print(a1)