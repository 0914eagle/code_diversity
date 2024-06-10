
import sys
input = sys.stdin.read()
P, R, L = map(int, input.split())
boulders = set(range(R))
planks = set()
for _ in range(L):
    endpoints = list(map(int, input.split()))
    planks.add(tuple(sorted(endpoints)))

def get_adjacent_boulders(boulder):
    return [b for b in boulders if (b, boulder) in planks or (boulder, b) in planks]

def dfs(boulder):
    if boulder == -1:
        return 1
    visited[boulder] = True
    count = 0
    for adjacent in get_adjacent_boulders(boulder):
        if not visited[adjacent]:
            count += dfs(adjacent)
    return count

visited = [False] * (R + 1)
count = dfs(-2)

if count >= P:
    print(count)
else:
    print(P - count)

