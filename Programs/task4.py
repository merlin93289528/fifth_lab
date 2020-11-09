n = int(input("n = "))
x = 1

x_1 = 1
x_2 = 1

for i in range(2, n + 1):
    x = x_1 + x_2
    x_2 = x_1
    x_1 = x

print(x)