import math

a = int(input("팩토리얼을 구할 숫자를 입력하세요 : "))

result = 1

for item in range(1, a+1):
    result *= item      #result = result * item
print(result)

# 혹은, math 라이브러리를 사용(import -> math()를 사용)
print(math.factorial(10))