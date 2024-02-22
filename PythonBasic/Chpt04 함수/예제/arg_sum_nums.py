def sum_nums(*args):
    a = 0
    for i in args:
        a += i
    print(a)


sum_nums(10,20,30)