
t = int(input())

for _ in range(t):
    input()  # empty line
    m, k = map(int, input().split())
    dishes = list(map(int, input().split()))
    
    available_dishes = [True] * k
    
    for _ in range(m - 1):
        t_j, r_j = map(int, input().split())
        if t_j != 0:
            if r_j == 1:
                available_dishes[t_j - 1] = False
    
    result = ""
    for dish in available_dishes:
        if dish:
            result += "Y"
        else:
            result += "N"
    
    print(result)
