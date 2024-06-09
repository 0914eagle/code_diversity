
import sys
input = sys.stdin.read()
input = input.split('\n')

n, m = map(int, input[0].split())

graph = {}
for i in range(1, n+1):
    graph[i] = []

for i in range(1, m+1):
    a, b, w = map(int, input[i].split())
    graph[a].append((b, w))
    graph[b].append((a, w))

q = int(input[m+1])

def find_path(s, t, visited, distance):
    if s == t:
        return distance
    
    for neighbor, w in graph[s]:
        if neighbor not in visited:
            visited.add(neighbor)
            distance = find_path(neighbor, t, visited, distance|w)
            visited.remove(neighbor)
    
    return distance

def f1(s, t):
    return find_path(s, t, set(), 0)

for i in range(q):
    s, t = map(int, input[m+2+i].split())
    print(f1(s, t))


