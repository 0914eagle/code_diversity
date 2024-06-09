
t = int(input())

for _ in range(t):
    input()  # empty line
    
    m, k = map(int, input().split())
    portions = list(map(int, input().split()))
    
    dish_status = ['Y'] * k
    
    for _ in range(m - 1):
        t_j, r_j = map(int, input().split())
        if t_j != 0:
            if r_j == 1:
                dish_status[t_j - 1] = 'N'
            else:
                portions[t_j - 1] -= 1
    
    for i in range(k):
        if portions[i] <= 0:
            dish_status[i] = 'Y'
    
    print(''.join(dish_status))
