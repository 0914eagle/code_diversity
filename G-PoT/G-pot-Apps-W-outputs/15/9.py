
n = int(input())
inventory_numbers = list(map(int, input().split()))

current_numbers = set()
for i in range(n):
    if inventory_numbers[i] in current_numbers:
        for j in range(1, n+1):
            if j not in current_numbers:
                inventory_numbers[i] = j
                current_numbers.add(j)
                break
    else:
        current_numbers.add(inventory_numbers[i])

print(*inventory_numbers)
