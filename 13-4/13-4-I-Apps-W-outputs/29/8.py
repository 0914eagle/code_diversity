
import sys

def get_inconvenience(bridges, collapsed_bridges):
    inconvenience = 0
    for bridge in bridges:
        if bridge[0] in collapsed_bridges or bridge[1] in collapsed_bridges:
            inconvenience += 1
    return inconvenience

n, m = map(int, input().split())
bridges = []
for _ in range(m):
    a, b = map(int, input().split())
    bridges.append((a, b))

collapsed_bridges = set()
inconvenience = 0
for i in range(m):
    collapsed_bridges.add(i+1)
    inconvenience = get_inconvenience(bridges, collapsed_bridges)
    print(inconvenience)

