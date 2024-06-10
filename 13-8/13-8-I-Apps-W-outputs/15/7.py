
def get_relatively_prime_graph(n, m):
    # Initialize an empty graph with n vertices and m edges
    graph = [[] for _ in range(n)]
    
    # Iterate through all possible edges
    for i in range(m):
        # Generate a random edge (u, v) such that GCD(u, v) = 1
        u, v = get_relatively_prime_edge(n)
        
        # Add the edge to the graph
        graph[u-1].append(v)
        graph[v-1].append(u)
    
    # Check if the graph is connected
    if not is_connected(graph):
        return "Impossible"
    
    # Return the graph
    return graph

def get_relatively_prime_edge(n):
    # Generate two random numbers between 1 and n
    u = random.randint(1, n)
    v = random.randint(1, n)
    
    # Check if GCD(u, v) = 1
    while math.gcd(u, v) != 1:
        u = random.randint(1, n)
        v = random.randint(1, n)
    
    # Return the edge (u, v)
    return u, v

def is_connected(graph):
    # Initialize a visited array and a queue
    visited = [False] * len(graph)
    queue = []
    
    # Enqueue the first vertex
    queue.append(0)
    visited[0] = True
    
    # Breadth-first search
    while queue:
        # Dequeue a vertex
        u = queue.pop(0)
        
        # Iterate through all neighbors of u
        for v in graph[u]:
            # If the neighbor has not been visited, mark it as visited and enqueue it
            if not visited[v-1]:
                visited[v-1] = True
                queue.append(v-1)
    
    # Check if all vertices have been visited
    return all(visited)

if __name__ == '__main__':
    n, m = map(int, input().split())
    graph = get_relatively_prime_graph(n, m)
    if graph == "Impossible":
        print("Impossible")
    else:
        print("Possible")
        for u, v in graph:
            print(u, v)

