
def is_bipartite(graph, start):
    color = {}
    stack = [(start, 0)]
    while stack:
        node, c = stack.pop()
        if node in color:
            if color[node] != c:
                return False
            continue
        color[node] = c
        for neighbor in graph[node]:
            stack.append((neighbor, c ^ 1))
    return True

def erase_elements(n, elements):
    elements.sort()
    graph = {i: [] for i in range(n)}
    for i in range(n):
        for j in range(i + 1, n):
            diff = abs(elements[i] - elements[j])
            if diff in elements:
                graph[i].append(j)
                graph[j].append(i)
    
    erased = set()
    for i in range(n):
        temp_graph = {k: v[:] for k, v in graph.items()}
        temp_elements = elements[:i] + elements[i+1:]
        for j in range(n):
            if j == i:
                continue
            for k in range(j + 1, n):
                diff = abs(temp_elements[j] - temp_elements[k])
                if diff in temp_elements:
                    temp_graph[j].append(k)
                    temp_graph[k].append(j)
        
        if is_bipartite(temp_graph, 0):
            erased.add(elements[i])
    
    print(len(erased))
    print(*erased)

if __name__ == "__main__":
    n = int(input())
    elements = list(map(int, input().split()))
    erase_elements(n, elements)
