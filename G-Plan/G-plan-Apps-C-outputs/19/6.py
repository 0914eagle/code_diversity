
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
    erased = set()
    graph = {i: set() for i in elements}
    
    for i in range(n):
        temp_graph = {i: set() for i in elements}
        temp_erased = set()
        
        for j in range(n):
            if i != j and abs(elements[i] - elements[j]) not in elements:
                temp_graph[elements[i]].add(elements[j])
        
        if is_bipartite(temp_graph, elements[i]):
            graph = temp_graph
            erased = temp_erased
    
    return len(erased), ' '.join(map(str, erased))

if __name__ == "__main__":
    n = int(input())
    elements = list(map(int, input().split()))
    k, erased_elements = erase_elements(n, elements)
    print(k)
    print(erased_elements)
