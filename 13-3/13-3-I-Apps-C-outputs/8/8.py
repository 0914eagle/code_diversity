
def f1(n, m, pairs):
    # Initialize a graph with n vertices and m edges
    graph = [[] for _ in range(n)]
    for p, q, c in pairs:
        graph[p - 1].append((q - 1, c))
        graph[q - 1].append((p - 1, c))
    
    # Use a union-find data structure to find the number of connected components in the graph
    from collections import defaultdict
    components = defaultdict(set)
    for i in range(n):
        components[i].add(i)
    for edge in graph:
        for i, j in edge:
            components[i].update(components[j])
    
    # If the graph has more than 1 connected component, it is not possible to arrange the students into groups of 2
    if len(components) > 1:
        return "impossible"
    
    # If the graph has 1 connected component, find the minimum total carbon dioxide emissions by arranging the students into groups of 2
    total_carbon_dioxide = 0
    for edge in graph:
        for i, j in edge:
            total_carbon_dioxide += edge[1]
    
    return total_carbon_dioxide

def f2(n, m, pairs):
    # Initialize a graph with n vertices and m edges
    graph = [[] for _ in range(n)]
    for p, q, c in pairs:
        graph[p - 1].append((q - 1, c))
        graph[q - 1].append((p - 1, c))
    
    # Use a union-find data structure to find the number of connected components in the graph
    from collections import defaultdict
    components = defaultdict(set)
    for i in range(n):
        components[i].add(i)
    for edge in graph:
        for i, j in edge:
            components[i].update(components[j])
    
    # If the graph has more than 1 connected component, it is not possible to arrange the students into groups of 2
    if len(components) > 1:
        return "impossible"
    
    # If the graph has 1 connected component, find the minimum total carbon dioxide emissions by arranging the students into groups of 2
    total_carbon_dioxide = 0
    for edge in graph:
        for i, j in edge:
            total_carbon_dioxide += edge[1]
    
    return total_carbon_dioxide

if __name__ == '__main__':
    n, m = map(int, input().split())
    pairs = []
    for _ in range(m):
        p, q, c = map(int, input().split())
        pairs.append((p, q, c))
    print(f1(n, m, pairs))
    print(f2(n, m, pairs))

