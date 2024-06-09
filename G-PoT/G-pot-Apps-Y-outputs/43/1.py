
S = input().strip()

price = 700
for char in S:
    if char == 'o':
        price += 100

print(price)
