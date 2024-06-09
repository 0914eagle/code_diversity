
def solve(N, R, flights, F, additional_flights):
    # Initialize a dictionary to store the cost of each flight
    costs = {}
    for flight in flights:
        costs[flight[0]] = flight[2]
    for flight in additional_flights:
        costs[flight[0]] = flight[2]
    
    # Initialize a graph with the airports as nodes
    graph = [[] for _ in range(N + 1)]
    for flight in flights:
        graph[flight[0]].append(flight[1])
        graph[flight[1]].append(flight[0])
    
    # Use Breadth-First Search to find the shortest path between all pairs of airports
    visited = [False] * (N + 1)
    queue = [1]
    visited[1] = True
    while queue:
        node = queue.pop(0)
        for neighbor in graph[node]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True
    
    # Calculate the total cost of the flights
    total_cost = 0
    for i in range(1, N + 1):
        for j in range(i + 1, N + 1):
            if costs[i] + costs[j] < total_cost:
                total_cost = costs[i] + costs[j]
    
    return total_cost

