
def f1(n, m, k, x_edges, y_edges, a_districts, b_districts):
    # Initialize graph with edge weights
    graph = {}
    for i in range(m):
        graph[x_edges[i]] = {y_edges[i]: w_edges[i]}
    
    # Find shortest path between each pair of districts
    shortest_paths = {}
    for i in range(n):
        shortest_paths[i] = dijkstra(graph, i)
    
    # Calculate total cost of each courier route
    total_costs = []
    for i in range(k):
        total_costs.append(shortest_paths[a_districts[i]][b_districts[i]])
    
    # Return minimum total cost
    return min(total_costs)

def f2(n, m, k, x_edges, y_edges, a_districts, b_districts):
    # Initialize graph with edge weights
    graph = {}
    for i in range(m):
        graph[x_edges[i]] = {y_edges[i]: w_edges[i]}
    
    # Find shortest path between each pair of districts
    shortest_paths = {}
    for i in range(n):
        shortest_paths[i] = dijkstra(graph, i)
    
    # Calculate total cost of each courier route
    total_costs = []
    for i in range(k):
        total_costs.append(shortest_paths[a_districts[i]][b_districts[i]])
    
    # Return minimum total cost
    return min(total_costs)

def dijkstra(graph, start):
    # Initialize priority queue with start vertex
    pq = [(0, start)]
    
    # Initialize distances with infinity
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    
    # Initialize previous vertices with None
    previous = {vertex: None for vertex in graph}
    
    # Loop until priority queue is empty
    while pq:
        # Get vertex with minimum distance from priority queue
        current_distance, current_vertex = heapq.heappop(pq)
        
        # If current vertex is not the destination, relax neighbors
        if current_vertex != destination:
            for neighbor, weight in graph[current_vertex].items():
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous[neighbor] = current_vertex
                    heapq.heappush(pq, (distance, neighbor))
    
    # Return distances and previous vertices
    return distances, previous

if __name__ == '__main__':
    n, m, k = map(int, input().split())
    x_edges = []
    y_edges = []
    w_edges = []
    for i in range(m):
        x, y, w = map(int, input().split())
        x_edges.append(x)
        y_edges.append(y)
        w_edges.append(w)
    a_districts = []
    b_districts = []
    for i in range(k):
        a, b = map(int, input().split())
        a_districts.append(a)
        b_districts.append(b)
    print(f1(n, m, k, x_edges, y_edges, a_districts, b_districts))
    print(f2(n, m, k, x_edges, y_edges, a_districts, b_districts))

