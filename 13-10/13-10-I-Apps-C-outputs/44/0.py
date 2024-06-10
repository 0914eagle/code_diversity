
def compute_non_similar_worlds(n, m):
    # Initialize a graph with two vertices, s and t, and no edges
    graph = {s: set(), t: set()}
    
    # Perform the given number of changes
    for i in range(n):
        # Add a new vertex to the graph
        w = len(graph)
        graph[w] = set()
        
        # Choose an existing edge (u, v) and add two new edges (u, w) and (v, w)
        u, v = choose_edge(graph)
        graph[u].add(w)
        graph[v].add(w)
        graph[w].add(u)
        graph[w].add(v)
    
    # Return the number of non-similar worlds, modulo 10^9 + 7
    return count_non_similar_worlds(graph, m)

def choose_edge(graph):
    # Choose an edge at random
    u, v = random.choice(list(graph.items()))
    return u, v

def count_non_similar_worlds(graph, m):
    # Initialize a variable to store the number of non-similar worlds
    non_similar_worlds = 0
    
    # Iterate over all possible bijections between the vertex sets of two worlds
    for f in itertools.permutations(graph.keys()):
        # Check if the bijection is a valid isomorphism
        if is_isomorphism(graph, f):
            # Increment the number of non-similar worlds
            non_similar_worlds += 1
    
    # Return the number of non-similar worlds, modulo 10^9 + 7
    return non_similar_worlds % (10**9 + 7)

def is_isomorphism(graph1, f):
    # Initialize a variable to store the second graph
    graph2 = {}
    
    # Create a dictionary mapping the vertices of the first graph to the corresponding vertices of the second graph
    for u in graph1:
        graph2[f(u)] = set()
    
    # Add edges to the second graph based on the bijection
    for u in graph1:
        for v in graph1[u]:
            graph2[f(u)].add(f(v))
    
    # Check if the second graph is isomorphic to the first graph
    return graph1 == graph2

if __name__ == '__main__':
    n, m = map(int, input().split())
    print(compute_non_similar_worlds(n, m))

