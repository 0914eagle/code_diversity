
def solve(N, V, edges):
    # Create a graph with N nodes and edges
    graph = [[] for _ in range(N+1)]
    for (a, b) in edges:
        graph[a].append(b)
    
    # Initialize a set to store the types of jokes seen
    jokes = set()
    
    # Function to recursively find the types of jokes seen by a person
    def dfs(node, supervisors):
        nonlocal jokes
        jokes.add(V[node])
        for supervisor in supervisors:
            dfs(supervisor, graph[supervisor])
    
    # Start the recursion with the CEO (node 1) and an empty set of supervisors
    dfs(1, graph[1])
    
    # Return the number of different types of jokes seen
    return len(jokes)

