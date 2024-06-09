
def f1(n, m, edges):
    # Initialize graph as a dictionary with each node as a key and its neighbors as values
    graph = {i: set() for i in range(n)}
    for i, j in edges:
        graph[i].add(j)
    
    # Initialize the set of source nodes (nodes with no incoming edges)
    sources = set(i for i in range(n) if not graph[i])
    
    # Initialize the list of sorted nodes
    sorted_nodes = []
    
    # While there are still source nodes, remove them and their outgoing edges, and add them to the list of sorted nodes
    while sources:
        source = sources.pop()
        sorted_nodes.append(source)
        for neighbor in graph[source]:
            graph[neighbor].remove(source)
            if not graph[neighbor]:
                sources.add(neighbor)
    
    # Return the largest possible size of S at the beginning of Step 1
    return len(sources)

def f2(n, m, edges):
    # Initialize graph as a dictionary with each node as a key and its neighbors as values
    graph = {i: set() for i in range(n)}
    for i, j in edges:
        graph[i].add(j)
    
    # Initialize the set of source nodes (nodes with no incoming edges)
    sources = set(i for i in range(n) if not graph[i])
    
    # Initialize the list of sorted nodes
    sorted_nodes = []
    
    # While there are still source nodes, remove them and their outgoing edges, and add them to the list of sorted nodes
    while sources:
        source = sources.pop()
        sorted_nodes.append(source)
        for neighbor in graph[source]:
            graph[neighbor].remove(source)
            if not graph[neighbor]:
                sources.add(neighbor)
    
    # Return the largest possible size of S at the beginning of Step 1
    return len(sources)

if __name__ == '__main__':
    n, m = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(m)]
    print(f1(n, m, edges))
    print(f2(n, m, edges))

