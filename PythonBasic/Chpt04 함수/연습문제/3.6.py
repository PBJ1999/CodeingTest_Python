def sort3(num1, num2, num3):
    numbers = []  # 숫자를 저장할 리스트에 인자들을 추가합니다.
    numbers.append(num1)
    numbers.append(num2)
    numbers.append(num3)

    # 오름차순으로 정렬
    numbers.sort()
    for i in range(0,3):
        print("오름차순으로 정렬된 숫자:", numbers[i])


# 함수 호출
num1 = int(input("첫 번째 숫자를 입력하세요: "))
num2 = int(input("두 번째 숫자를 입력하세요: "))
num3 = int(input("세 번째 숫자를 입력하세요: "))
sort3(num1, num2, num3)