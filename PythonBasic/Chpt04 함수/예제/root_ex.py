a,b,c = map(int, input().split())

# (a * x ^ 2) + ( b * x ) + c = 0

r1 = (-b + (b ** 2 - 4 * a * c)** 0.5) / (2 * a)
r2 = (-b - (b ** 2 - 4 * a * c)** 0.5) / (2 * a)

print(r1, r2)