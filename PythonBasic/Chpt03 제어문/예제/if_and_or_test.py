a, b = map(int, input().split())

# and와 or로 두 수의 정의를 가리자(홀,짝)


if (a % 2 == 0) and (b % 2 == 0):
    print("두 수는 짝수입니다.")
elif (a % 2 == 0) or (b % 2 == 0):
    print("하나만 짝수입니다.")
else:
    print("둘 다 홀수이거나, 잘 못 입력된 값입니다.")