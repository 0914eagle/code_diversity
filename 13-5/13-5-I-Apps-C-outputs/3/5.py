
def solve_problem(n, m, s, t, edges):
    # Initialize the graph with the given edges
    graph = [[] for _ in range(n)]
    for u, v, c in edges:
        graph[u].append((v, c))
    
    # Initialize the flow graph with the given source and sink
    flow_graph = [[] for _ in range(n)]
    flow_graph[s].append((t, 0))
    
    # Initialize the maximum flow and the number of edges used
    max_flow = 0
    num_edges = 0
    
    # Repeat the following until there are no more edges to be added
    while True:
        # Find an augmenting path in the flow graph
        path = find_augmenting_path(flow_graph, s, t)
        if not path:
            break
        
        # Add the path to the maximum flow and the number of edges used
        max_flow += add_path(flow_graph, path)
        num_edges += 1
    
    # Return the maximum flow and the number of edges used
    return max_flow, num_edges

def find_augmenting_path(flow_graph, s, t):
    # Initialize the queue with the source node
    queue = [s]
    
    # Initialize the visited array with False values
    visited = [False] * len(flow_graph)
    
    # Repeat the following until the queue is empty
    while queue:
        # Get the current node from the queue
        node = queue.pop(0)
        
        # If the current node is the sink, return the path
        if node == t:
            path = []
            while node != s:
                path.append(node)
                node = parent[node]
            return path[::-1]
        
        # If the current node has not been visited, mark it as visited and add its neighbors to the queue
        if not visited[node]:
            visited[node] = True
            for neighbor, capacity in flow_graph[node]:
                if not visited[neighbor]:
                    queue.append(neighbor)
    
    # If no path is found, return an empty list
    return []

def add_path(flow_graph, path):
    # Initialize the maximum flow and the number of edges used
    max_flow = 0
    num_edges = 0
    
    # Repeat the following for each edge in the path
    for i in range(len(path) - 1):
        # Get the current edge
        u, v = path[i], path[i + 1]
        
        # If the capacity of the edge is not exhausted, add the minimum of the residual capacity and the maximum flow to the flow graph
        if flow_graph[u][v][1] > 0:
            flow = min(flow_graph[u][v][1], max_flow)
            flow_graph[u][v][1] -= flow
            flow_graph[v][u][1] += flow
            max_flow -= flow
            num_edges += 1
    
    # Return the maximum flow and the number of edges used
    return max_flow, num_edges

# Test the solve_problem function with the given example
n = 4
m = 5
s = 0
t = 3
edges = [(0, 1, 10), (1, 2, 1), (1, 3, 1), (0, 2, 1), (2, 3, 10)]
max_flow, num_edges = solve_problem(n, m, s, t, edges)
print(max_flow, num_edges)
for u, v, c in edges:
    if c > 0:
        print(u, v, c)

