
N, *T = [int(x) for x in input().split()]
M, *PX = [int(x) for x in input().split()]

drinks = []
for i in range(M):
    P, X = PX[i*2], PX[i*2+1]
    drinks.append((P, X))

total_time = sum(T)
for P, X in drinks:
    new_time = total_time
    for i in range(N):
        if i+1 == P:
            new_time -= T[i]
            new_time += X
    print(new_time)

