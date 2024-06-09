
n = int(input())

for i in range(n):
    k = int(input())
    menu_items = []
    for j in range(k):
        menu_item = input()
        menu_items.append(menu_item)
    if "pea soup" in menu_items and "pancakes" in menu_items:
        print(menu_items[0])
        break
else:
    print("Anywhere is fine I guess")

