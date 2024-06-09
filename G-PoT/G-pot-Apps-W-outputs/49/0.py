
t = int(input())

for _ in range(t):
    input()  # empty line
    
    m, k = map(int, input().split())
    dishes = list(map(int, input().split()))
    
    available = [True] * k
    
    for _ in range(m - 1):
        t_j, r_j = map(int, input().split())
        if t_j != 0:
            if r_j == 1:
                available[t_j - 1] = False
    
    output = ""
    for dish in available:
        if dish:
            output += "Y"
        else:
            output += "N"
    
    print(output)
