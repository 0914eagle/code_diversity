
t = int(input())

for _ in range(t):
    input()  # empty line
    
    m, k = map(int, input().split())
    portions = list(map(int, input().split()))
    
    remaining_portions = portions.copy()
    
    for _ in range(m - 1):
        dish, disappointed = map(int, input().split())
        if dish != 0 and not disappointed:
            remaining_portions[dish - 1] -= 1
    
    result = ""
    for i in range(k):
        if remaining_portions[i] < m - remaining_portions[i]:
            result += "Y"
        else:
            result += "N"
    
    print(result)
