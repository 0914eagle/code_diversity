
def count_simple_loops(m, connections):
    def dfs(node, visited, start, count):
        visited[node] = True
        if len(visited) == m and start in connections[node]:
            count[0] += 1
        for neighbor in connections[node]:
            if not visited[neighbor]:
                dfs(neighbor, visited.copy(), start, count)
    
    count = [0]
    for i in range(m):
        visited = [False] * m
        dfs(i, visited, i, count)
    
    return count[0]

# Read input
m = int(input())
n = int(input())
connections = {i: [] for i in range(m)}
for _ in range(n):
    s, t = map(int, input().split())
    connections[s].append(t)

# Count unique simple loops
result = count_simple_loops(m, connections)
print(result)
