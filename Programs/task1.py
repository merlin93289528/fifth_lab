a = float(input("a = "))
n = int(input("n = "))

product = 1
exp = a

for i in range(0, n):
    exp = a + i
    product *= exp ** 2

print(product)