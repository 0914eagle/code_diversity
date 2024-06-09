
def solve(flights, additional_flights):
    # Initialize a dictionary to store the cost of each flight
    flight_costs = {}
    for flight in flights:
        cost = flight[2]
        flight_costs[(flight[0], flight[1])] = cost
        flight_costs[(flight[1], flight[0])] = cost

    # Add the additional flights to the dictionary
    for flight in additional_flights:
        cost = flight[2]
        flight_costs[(flight[0], flight[1])] = cost
        flight_costs[(flight[1], flight[0])] = cost

    # Find the shortest path using Dijkstra's algorithm
    from collections import deque
    import heapq
    queue = deque([(1, 0)])
    visited = set()
    while queue:
        city, cost = heapq.heappop(queue)
        if city == 1:
            return cost
        if city in visited:
            continue
        visited.add(city)
        for neighbor, weight in flight_costs.items():
            if neighbor[0] == city:
                heapq.heappush(queue, (neighbor[1], cost + weight))
    return -1

