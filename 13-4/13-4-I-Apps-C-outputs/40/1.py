
N, M, Q = map(int, input().split())

teachers = list(range(1, N+1))
classes = list(range(1, N+1))

schedule = [[0] * M for _ in range(N)]

for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 0:
        # Add a reassignment plan
        K, x, *p = query
        for i in range(K):
            schedule[p[i]-1][x-1] = p[(i+1)%K]
    else:
        # Ask a question
        d, x = query[1:]
        print(schedule[d-1][x-1])

