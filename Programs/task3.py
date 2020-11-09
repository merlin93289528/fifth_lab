from math import log, cos

x = float(input("Введіть х: "))
eps = float(input("Задайте точність: "))

summ = 0
exp = log(2)
n = 0

while exp > eps:
    summ -= exp
    n += 1
    exp = cos(x * n) / n

print(summ)