
def count_simple_loops():
    m = int(input())
    n = int(input())
    connections = []
    for _ in range(n):
        s, t = map(int, input().split())
        connections.append((s, t))
    
    def dfs(node, visited, start_node, length):
        if length > 1 and node == start_node:
            return 1
        if length == m:
            return 0
        
        count = 0
        for s, t in connections:
            if s == node and t not in visited:
                count += dfs(t, visited + [t], start_node, length + 1)
        
        return count
    
    total_loops = 0
    for i in range(m):
        total_loops += dfs(i, [i], i, 1)
    
    print(total_loops)

count_simple_loops()
