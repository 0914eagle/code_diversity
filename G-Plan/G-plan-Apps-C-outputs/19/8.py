
def is_bipartite(graph, start):
    colors = {}
    stack = [(start, 0)]
    
    while stack:
        node, color = stack.pop()
        if node in colors:
            if colors[node] != color:
                return False
            continue
        
        colors[node] = color
        next_color = 1 - color
        for neighbor in graph.get(node, []):
            stack.append((neighbor, next_color))
    
    return True

def erase_subset(n, b):
    b.sort()
    graph = {}
    erased = set()
    
    for i in range(n):
        temp_graph = graph.copy()
        temp_erased = set(erased)
        
        for j in range(i):
            if b[i] - b[j] not in temp_graph:
                temp_graph[b[i] - b[j]] = []
            temp_graph[b[i] - b[j]].append(b[j])
        
        if is_bipartite(temp_graph, b[i]):
            graph = temp_graph
        else:
            erased.add(b[i])
    
    return len(erased), list(erased)

if __name__ == "__main__":
    n = int(input())
    b = list(map(int, input().split()))
    k, erased_elements = erase_subset(n, b)
    print(k)
    print(*erased_elements)
