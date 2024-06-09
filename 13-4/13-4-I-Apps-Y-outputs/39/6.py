
N, *T = [int(x) for x in input().split()]
M, *PX = [int(x) for x in input().split()]

def get_time(P, X):
    return sum(T[i-1] if i != P else T[i-1] + X for i in range(1, N+1))

for i in range(M):
    print(get_time(PX[i*2-1], PX[i*2]))

