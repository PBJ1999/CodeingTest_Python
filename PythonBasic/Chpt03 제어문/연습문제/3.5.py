a, b = map(int, input().split())

if a % b == 0:
    print("{}는 {}의 배수입니다.".format(a,b))
else:
    print("{}는 {}의 배수가 아닙니다.".format(a, b))