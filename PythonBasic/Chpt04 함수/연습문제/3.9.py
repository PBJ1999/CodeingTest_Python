def sum_range(n1, n2):
    if n1 >= n2:
        print("error")
    else:
        return sum(range(n1, n2 + 1))


print("10~20까지의 정수의 합: {}".format(sum_range(10, 20)))
print("40~200까지의 정수의 합: {}".format(sum_range(40, 200)))
