def my_sorts(*args):
    num = [] # 빈 배열 만들기
    for i in args:
        num.append(i) # 반복문으로 args의 임의의변수들을 append()
    num.sort() # 마지막으로 순서대로 정렬(오름차순)

    print("result: {}".format(num))


my_sorts(45,3,4,56,5)
