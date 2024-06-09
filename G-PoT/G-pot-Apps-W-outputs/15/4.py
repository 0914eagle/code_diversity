
n = int(input())
inventory_numbers = list(map(int, input().split()))

unique_numbers = set()
for i in range(n):
    if inventory_numbers[i] in unique_numbers:
        for j in range(1, n + 1):
            if j not in unique_numbers:
                inventory_numbers[i] = j
                unique_numbers.add(j)
                break
    else:
        unique_numbers.add(inventory_numbers[i])

print(*inventory_numbers)
