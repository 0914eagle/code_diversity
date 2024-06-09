
t = int(input())

for _ in range(t):
    input()  # empty line
    m, k = map(int, input().split())
    portions = list(map(int, input().split()))
    
    remaining_portions = portions.copy()
    
    for _ in range(m - 1):
        t_j, r_j = map(int, input().split())
        if t_j != 0 and r_j == 0:
            remaining_portions[t_j - 1] -= 1
    
    result = ''
    for i in range(k):
        if remaining_portions[i] <= 0:
            result += 'Y'
        else:
            result += 'N'
    
    print(result)
