
import sys

def get_inconvenience(bridges, i):
    inconvenience = 0
    for bridge in bridges[:i]:
        inconvenience += len(set([bridge[0], bridge[1]]))
    return inconvenience

n, m = map(int, input().split())
bridges = []
for _ in range(m):
    a, b = map(int, input().split())
    bridges.append((a, b))

for i in range(1, m+1):
    print(get_inconvenience(bridges, i))

