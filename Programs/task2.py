n = int(input("n = "))

num_of_one = 0

while n != 0:

    if n % 10 == 1:
        num_of_one += 1

    n = int(n/10)

print(f"Одиниць в числі: {num_of_one}")