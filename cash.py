count = 0
remaining = -1

while remaining < 0:
    try:
        remaining = float(input("Change: "))
        remaining *= 100
    except ValueError:
        print("Please enter a number.")

coins = [25, 10, 5, 1]

for i in range(4):
    while remaining - coins[i] >= 0:
        remaining -= coins[i]
        count += 1

print(count)
