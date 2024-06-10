
def find_good_nodes(n, edges):
    graph = {}
    for i in range(1, n + 1):
        graph[i] = []
    
    for a, b, c in edges:
        graph[a].append((b, c))
        graph[b].append((a, c))
    
    def is_rainbow_path(node, parent_color):
        for neighbor, color in graph[node]:
            if color == parent_color:
                return False
            if not is_rainbow_path(neighbor, color):
                return False
        return True
    
    good_nodes = []
    for node in range(1, n + 1):
        if is_rainbow_path(node, -1):
            good_nodes.append(node)
    
    return good_nodes

if __name__ == '__main__':
    n = int(input())
    edges = [list(map(int, input().split())) for _ in range(n - 1)]
    
    good_nodes = find_good_nodes(n, edges)
    
    print(len(good_nodes))
    for node in good_nodes:
        print(node)
