ve_leaves_to_eliminate_sadness(n, vertices, edges):
    tree = {}
    for i in range(1, n + 1):
        tree[i] = {'value': vertices[i - 1], 'children': []}
    
    for p, c in edges:
        tree[p]['children'].append(c)
    
    def dfs(node):
        if not tree[node]['children']:
            return 0
        
        max_distance = 0
        for child in tree[node]['children']:
            max_distance = max(max_distance, dfs(child) + tree[child]['value'])
        
        return max_distance
    
    def identify_sad_vertices():
        def is_sad(node):
            if not tree[node]['children']:
                return False
            
            for child in tree[node]['children']:
                if dfs(child) + tree[child]['value'] > tree[node]['value']:
                    return True
            
            return any(is_sad(child) for child in tree[node]['children'])
        
        return [node for node in tree if is_sad(node)]
    
    def remove_leaves(sad_vertices):
        leaves_to_remove = 0
        for vertex in sad_vertices:
            if not tree[vertex]['children']:
                leaves_to_remove += 1
        
        return leaves_to_remove
    
    sad_vertices = identify_sad_vertices()
    leaves_to_remove = remove_leaves(sad_vertices)
    
    return leaves_to_remove


if __name__ == "__main__":
    n = int(input())
    vertices = list(map(int, input().split()))
    edges = [list(map(int, input().split())) for _ in range(n - 1)]
    
    result = remove_leaves_to_eliminate_sadness(n, vertices, edges)
    print(result)
