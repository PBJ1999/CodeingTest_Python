def min_nums(*args):
    if len(args) == 0:
        print("인자가 없습니다.")
    else:
        min_value = args[0]  # 가변인자 중 첫 번째 값을 최소값으로 초기화
        for num in args:
            if num < min_value:
                min_value = num
        print("최솟값은 {}입니다.".format(min_value))

# 함수 호출
min_nums(10, 20, 30)