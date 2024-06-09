
N, M = map(int, input().split())
elevations = list(map(int, input().split()))

reachable_from = [set() for _ in range(N)]
for _ in range(M):
    A, B = map(int, input().split())
    reachable_from[A-1].add(B-1)
    reachable_from[B-1].add(A-1)

good_obs = 0
for i in range(N):
    is_good = True
    for neighbor in reachable_from[i]:
        if elevations[i] <= elevations[neighbor]:
            is_good = False
            break
    if is_good:
        good_obs += 1

print(good_obs)
