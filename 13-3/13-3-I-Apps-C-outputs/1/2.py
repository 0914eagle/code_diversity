
def f1(n, m, edges):
    # Initialize graph as a dictionary with node as key and its neighbors as value
    graph = {i: set() for i in range(n)}
    for i, j in edges:
        graph[i].add(j)
    
    # Initialize S as the set of source nodes
    S = set(i for i in range(n) if not graph[i])
    
    # Initialize L as an empty list
    L = []
    
    # While S is not empty
    while S:
        # Choose an arbitrary node from S
        alpha = S.pop()
        
        # Remove alpha and its outgoing edges from the graph
        for neighbor in graph[alpha]:
            graph[neighbor].remove(alpha)
            if not graph[neighbor]:
                S.add(neighbor)
        
        # Insert alpha at the end of L
        L.append(alpha)
    
    # Return the largest possible size of S at the beginning of Step 1
    return len(S)

def f2(n, m, edges):
    # Initialize graph as a dictionary with node as key and its neighbors as value
    graph = {i: set() for i in range(n)}
    for i, j in edges:
        graph[i].add(j)
    
    # Initialize S as the set of source nodes
    S = set(i for i in range(n) if not graph[i])
    
    # Initialize L as an empty list
    L = []
    
    # While S is not empty
    while S:
        # Choose an arbitrary node from S
        alpha = S.pop()
        
        # Remove alpha and its outgoing edges from the graph
        for neighbor in graph[alpha]:
            graph[neighbor].remove(alpha)
            if not graph[neighbor]:
                S.add(neighbor)
        
        # Insert alpha at the end of L
        L.append(alpha)
    
    # Return the largest possible size of S at the beginning of Step 1
    return len(S)

if __name__ == '__main__':
    n, m = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(m)]
    print(f1(n, m, edges))
    print(f2(n, m, edges))

