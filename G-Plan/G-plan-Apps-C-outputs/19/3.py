
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
        
        for neighbor in graph[node]:
            stack.append((neighbor, 1 - color))
    
    return True

def erase_elements(n, elements):
    elements.sort()
    graph = {i: [] for i in elements}
    
    for i in range(n):
        for j in range(i + 1, n):
            diff = abs(elements[i] - elements[j])
            if diff in elements:
                graph[elements[i]].append(elements[j])
                graph[elements[j]].append(elements[i])
    
    erased = set()
    for element in elements:
        graph_copy = {k: v[:] for k, v in graph.items()}
        graph_copy.pop(element)
        
        if is_bipartite(graph_copy, elements[0]):
            erased.add(element)
    
    return len(erased), " ".join(map(str, erased))

if __name__ == "__main__":
    n = int(input())
    elements = list(map(int, input().split()))
    
    k, erased_elements = erase_elements(n, elements)
    print(k)
    print(erased_elements)
