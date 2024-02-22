# 1. year 변수를 정수로 입력받는다.
year = int(input())

# 2. 윤년 판단 조건문을 세운다.
if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
    # 3-1. 윤년 판단 조건에 따라 출력을 한다.
    print('yes')
else:
    # 3-2. 윤년 판단 조건에 따라 출력을 한다.
    print('no')