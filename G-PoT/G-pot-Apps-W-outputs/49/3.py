
t = int(input())

for _ in range(t):
    input()  # empty line
    m, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    dish_available = [True] * k
    
    for _ in range(m - 1):
        t_j, r_j = map(int, input().split())
        if t_j != 0:
            if r_j == 1:
                dish_available[t_j - 1] = False
    
    result = ""
    for dish in dish_available:
        if dish:
            result += "Y"
        else:
            result += "N"
    
    print(result)
