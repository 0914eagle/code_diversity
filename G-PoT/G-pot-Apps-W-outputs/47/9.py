
def count_simple_loops(m, connections):
    def dfs(node, visited, start_node, length):
        if length > 1 and node == start_node:
            return 1
        if length == m:
            return 0
        
        visited[node] = True
        total = 0
        for neighbor in connections[node]:
            if not visited[neighbor]:
                total += dfs(neighbor, visited.copy(), start_node, length + 1)
        
        return total
    
    total_loops = 0
    for i in range(m):
        visited = [False] * m
        total_loops += dfs(i, visited, i, 0)
    
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
