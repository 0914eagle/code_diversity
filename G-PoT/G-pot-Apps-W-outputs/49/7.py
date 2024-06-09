
t = int(input())

for _ in range(t):
    input()  # empty line
    m, k = map(int, input().split())
    dishes = list(map(int, input().split()))
    
    remaining_dishes = dishes.copy()
    possible = ['Y'] * k
    
    for _ in range(m - 1):
        t_j, r_j = map(int, input().split())
        if t_j != 0:
            if r_j == 1:
                remaining_dishes[t_j - 1] -= 1
            else:
                possible[t_j - 1] = 'N'
    
    for i in range(k):
        if sum(remaining_dishes) - remaining_dishes[i] < m:
            possible[i] = 'Y'
    
    print(''.join(possible))
