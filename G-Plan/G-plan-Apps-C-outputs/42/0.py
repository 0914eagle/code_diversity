
def good_nodes_in_tree(n, edges):
    graph = {i: [] for i in range(1, n + 1)}
    colors = {}
    
    for a, b, c in edges:
        graph[a].append((b, c))
        graph[b].append((a, c))
    
    def is_rainbow_path(node, parent_color):
        for neighbor, color in graph[node]:
            if neighbor != parent_color:
                if colors.get((node, neighbor)) == color:
                    return False
                colors[(node, neighbor)] = color
                colors[(neighbor, node)] = color
                if not is_rainbow_path(neighbor, node):
                    return False
        return True
    
    good_nodes = []
    for i in range(1, n + 1):
        if is_rainbow_path(i, 0):
            good_nodes.append(i)
    
    return len(good_nodes), good_nodes

if __name__ == '__main__':
    n = int(input())
    edges = [list(map(int, input().split())) for _ in range(n - 1)]
    
    k, good_nodes = good_nodes_in_tree(n, edges)
    print(k)
    for node in good_nodes:
        print(node)
