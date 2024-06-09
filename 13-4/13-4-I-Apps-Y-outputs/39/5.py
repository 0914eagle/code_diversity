
N, *T = [int(x) for x in input().split()]
M, *PX = [int(x) for x in input().split()]

result = []
for i in range(M):
    P, X = PX[i*2], PX[i*2+1]
    time = 0
    for j in range(N):
        if j+1 == P:
            time += X
        else:
            time += T[j]
    result.append(time)

for r in result:
    print(r)

