a = (1,2,3,4,5)

a1 = a[0]
a2 = a[1]

# packing: 하나의 튜플 변수에 여러개의 값을 넣는 걸 의미한다.

# unpacking: 튜플 변수로부터 여러개의 값을 개별 변수에 담아 출력하는 걸 의미한다.

b =1,2 # 튜플 변수 b로

d,e = b # 개별 변수 d,e에 각 값을 넣고

print(d,e) # 출력

swap = d
d = e
e = swap

print(d,e)