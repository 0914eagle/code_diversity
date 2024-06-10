
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
        temp_graph = {k: v.copy() for k, v in graph.items()}
        temp_graph.pop(element)
        
        if is_bipartite(temp_graph, elements[0]):
            erased.add(element)
    
    print(len(erased))
    print(*erased)

if __name__ == "__main__":
    n = int(input())
    elements = list(map(int, input().split()))
    erase_elements(n, elements)
