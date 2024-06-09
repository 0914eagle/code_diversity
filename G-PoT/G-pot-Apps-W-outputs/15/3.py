
n = int(input())
inventory = list(map(int, input().split()))

inventory_set = set(inventory)
missing_numbers = list(set(range(1, n + 1)) - inventory_set)

for i in range(n):
    if inventory[i] in missing_numbers:
        inventory[i] = missing_numbers.pop(0)

print(*inventory)
