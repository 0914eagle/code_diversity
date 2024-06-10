
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
    erased = set()
    
    for i in range(n):
        for j in range(i + 1, n):
            diff = abs(elements[i] - elements[j])
            if diff not in elements:
                erased.add(elements[i])
                break
            graph[elements[i]].append(elements[j])
            graph[elements[j]].append(elements[i])
    
    for element in elements:
        if element in erased:
            continue
        
        if not is_bipartite(graph, element):
            erased.add(element)
    
    return len(erased), erased

if __name__ == "__main__":
    n = int(input())
    elements = list(map(int, input().split()))
    
    k, erased_elements = erase_elements(n, elements)
    print(k)
    for element in erased_elements:
        print(element)
