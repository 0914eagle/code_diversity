
def count_simple_loops(m, connections):
    def dfs(node, visited, start_node, length):
        if length > 1 and node == start_node:
            return 1
        if length == m:
            return 0
        count = 0
        visited[node] = True
        for neighbor in connections[node]:
            if not visited[neighbor]:
                count += dfs(neighbor, visited.copy(), start_node, length + 1)
        return count

    total_loops = 0
    for i in range(m):
        visited = [False] * m
        total_loops += dfs(i, visited, i, 0)
    return total_loops

m = int(input())
n = int(input())
connections = [[] for _ in range(m)]
for _ in range(n):
    s, t = map(int, input().split())
    connections[s].append(t)

print(count_simple_loops(m, connections))
