def calculate_statistics(*numbers):
    if not numbers:
        print("입력된 숫자가 없습니다.")
        pass

    min_value = min(numbers)
    max_value = max(numbers)
    average = sum(numbers) / len(numbers)

    print("최솟값: {}".format(min_value))
    print("최댓값: {}".format(max_value))
    print("평균값: {}".format(average))


# 함수 호출
# map(int, input().split())을 통해 정수로 변환한 뒤에도 리스트 형태로 전달되지 않는다는 점
# list(map(int, input().split())) => 정당한 사용법
user_input = list(map(int, input().split()))
calculate_statistics(*user_input)

