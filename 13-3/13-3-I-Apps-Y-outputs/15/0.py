
n = int(input())

for i in range(n):
    k = int(input())
    menu = []
    for j in range(k+1):
        menu.append(input())
    
    if "pea soup" in menu and "pancakes" in menu:
        print(menu[0])
        break
else:
    print("Anywhere is fine I guess")

