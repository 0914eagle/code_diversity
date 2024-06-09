
import sys
input = sys.stdin.read()
n, m = map(int, input.split())
brain_connectors = []

for i in range(m):
    brain_connectors.append(list(map(int, input.split())))

brain_latency = 0
for i in range(n):
    for j in range(i, n):
        if j > i:
            distance = 0
            for connector in brain_connectors:
                if connector[0] == i and connector[1] == j:
                    distance += 1
                elif connector[0] == j and connector[1] == i:
                    distance += 1
            if distance > brain_latency:
                brain_latency = distance

print(brain_latency)

