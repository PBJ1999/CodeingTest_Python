def square(x,y):
    x1 = x ** 2
    y1 = y ** 2
    return x1,y1


x = 10
y = 20

x_sq, y_sq = square(x,y)

print("{}의 제곱 = {}, {}의 제곱 = {}".format(x,x_sq,y,y_sq))