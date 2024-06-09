
A = int(input())
B = int(input())

N = A + B + 1

if A == 0:
    stops = list(range(2, N+1))
    stops.append(1)
else:
    stops = [1]
    for i in range(2, N):
        if i % 2 == 0:
            stops.append(i)
    stops.append(N)

print(*stops)
