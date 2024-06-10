
def remove_leaves(n, vertex_values, edges):
    tree = {}
    for i in range(1, n+1):
        tree[i] = {'value': vertex_values[i-1], 'children': []}
    
    for p, c in edges:
        tree[p]['children'].append(c)
    
    def dfs(node):
        if not tree[node]['children']:
            return 0, 0
        
        max_dist = 0
        total_leaves_removed = 0
        for child in tree[node]['children']:
            child_max_dist, child_leaves_removed = dfs(child)
            max_dist = max(max_dist, child_max_dist + tree[child]['value'])
            total_leaves_removed += child_leaves_removed
        
        if max_dist > tree[node]['value']:
            total_leaves_removed += 1
        
        return max_dist, total_leaves_removed
    
    _, leaves_removed = dfs(1)
    return leaves_removed

if __name__ == "__main__":
    n = int(input())
    vertex_values = list(map(int, input().split()))
    edges = [list(map(int, input().split())) for _ in range(n-1)]
    
    print(remove_leaves(n, vertex_values, edges))
