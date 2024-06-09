
n = int(input())
inventory_numbers = list(map(int, input().split()))

unique_numbers = set(inventory_numbers)
missing_numbers = set(range(1, n + 1)) - unique_numbers

for i in range(n):
    if inventory_numbers[i] in missing_numbers:
        inventory_numbers[i] = missing_numbers.pop()

print(*inventory_numbers)
