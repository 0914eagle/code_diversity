
import sys

def get_inconvenience(n, m, bridges):
    # Initialize a dictionary to store the pairs of islands that are no longer connected
    inconvenience = {}
    
    # Iterate through the bridges and mark the pairs of islands that are no longer connected
    for i in range(m):
        a, b = bridges[i]
        if a not in inconvenience:
            inconvenience[a] = []
        if b not in inconvenience:
            inconvenience[b] = []
        inconvenience[a].append(b)
        inconvenience[b].append(a)
    
    # Count the number of pairs of islands that are no longer connected
    count = 0
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if i not in inconvenience or j not in inconvenience[i]:
                count += 1
    
    return count

n, m = map(int, input().split())
bridges = []
for i in range(m):
    a, b = map(int, input().split())
    bridges.append((a, b))

print(*[get_inconvenience(n, m, bridges[:i + 1]) for i in range(m)], sep='\n')

