
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
        
        for neighbor in graph[node]:
            stack.append((neighbor, next_color))
    
    return True

def erase_elements(n, elements):
    elements.sort()
    graph = {i: [] for i in elements}
    
    for i in range(n):
        for j in range(i + 1, n):
            diff = abs(elements[i] - elements[j])
            if diff not in elements:
                graph[elements[i]].append(elements[j])
                graph[elements[j]].append(elements[i])
    
    erased = set()
    for element in elements:
        temp_graph = {key: value[:] for key, value in graph.items()}
        temp_graph.pop(element)
        
        if all(is_bipartite(temp_graph, node) for node in temp_graph):
            erased.add(element)
    
    return len(erased), ' '.join(map(str, erased))

if __name__ == "__main__":
    n = int(input())
    elements = list(map(int, input().split()))
    k, erased_elements = erase_elements(n, elements)
    print(k)
    print(erased_elements)