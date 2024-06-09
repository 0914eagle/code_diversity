
N, M = map(int, input().split())
H = list(map(int, input().split()))
roads = [list(map(int, input().split())) for _ in range(M)]

reachable = set()
for a, b in roads:
    if H[a-1] < H[b-1]:
        reachable.add(a)
    elif H[a-1] > H[b-1]:
        reachable.add(b)

good_obs = 0
for i in range(1, N+1):
    if i not in reachable:
        good_obs += 1

print(good_obs)
