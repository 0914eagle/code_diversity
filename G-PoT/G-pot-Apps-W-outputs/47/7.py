
def count_simple_loops(m, connections):
    def dfs(node, visited, start):
        visited[node] = True
        if len(visited) == m and start in connections[node]:
            return 1
        count = 0
        for neighbor in connections[node]:
            if not visited[neighbor]:
                count += dfs(neighbor, visited.copy(), start)
        return count

    total_loops = 0
    for i in range(m):
        visited = [False] * m
        total_loops += dfs(i, visited, i)
    
    return total_loops

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
