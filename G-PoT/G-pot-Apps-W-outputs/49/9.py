
t = int(input())

for _ in range(t):
    input()  # empty line
    m, k = map(int, input().split())
    dishes = list(map(int, input().split()))
    
    remaining_dishes = dishes.copy()
    
    for _ in range(m - 1):
        t_j, r_j = map(int, input().split())
        if t_j != 0 and r_j == 0:
            remaining_dishes[t_j - 1] -= 1
    
    output = ""
    for dish in remaining_dishes:
        if dish <= 0:
            output += "Y"
        else:
            output += "N"
    
    print(output)
