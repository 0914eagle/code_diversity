
def solve(n, flights):
    # Initialize a graph with the given flights
    graph = {i: set() for i in range(1, n + 1)}
    for flight in flights:
        graph[flight[0]].add(flight[1])
        graph[flight[1]].add(flight[0])

    # Find the flight with the maximum number of changes
    max_changes = 0
    flight_to_cancel = None
    for city in graph:
        changes = 0
        for neighbor in graph[city]:
            if neighbor != city:
                changes += 1
        if changes > max_changes:
            max_changes = changes
            flight_to_cancel = city

    # Find the city pair with the minimum number of changes
    min_changes = float('inf')
    city_pair = None
    for city1 in graph:
        for city2 in graph[city1]:
            if city1 < city2 and graph[city2].issuperset({city1}):
                changes = 0
                for neighbor in graph[city1]:
                    if neighbor != city1 and neighbor != city2:
                        changes += 1
                for neighbor in graph[city2]:
                    if neighbor != city1 and neighbor != city2:
                        changes += 1
                if changes < min_changes:
                    min_changes = changes
                    city_pair = (city1, city2)

    return [max_changes, flight_to_cancel, city_pair]

