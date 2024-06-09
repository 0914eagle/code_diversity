
def solve(flights, additional_flights):
    # Initialize a dictionary to store the cost of each flight
    flight_costs = {}
    for flight in flights:
        flight_costs[flight] = flights[flight]
    for flight in additional_flights:
        flight_costs[flight] = additional_flights[flight]
    
    # Find the shortest path using Dijkstra's algorithm
    start = 1
    end = 1
    visited = set()
    queue = [(0, start)]
    while queue:
        cost, node = heapq.heappop(queue)
        if node not in visited:
            visited.add(node)
            if node == end:
                return cost
            for neighbor, weight in flight_costs[node].items():
                if neighbor not in visited:
                    heapq.heappush(queue, (cost + weight, neighbor))
    
    return -1

