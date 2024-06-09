
n = int(input())
items = list(map(int, input().split()))

inventory = {}
new_inventory = []
next_number = 1

for item in items:
    if item not in inventory:
        inventory[item] = True
        new_inventory.append(item)
    else:
        while next_number in inventory:
            next_number += 1
        new_inventory.append(next_number)
        next_number += 1

print(*new_inventory)
