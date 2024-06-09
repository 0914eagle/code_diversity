
def solve(n, m, train_lines):
    # Initialize a graph with the given number of cities
    graph = [[] for _ in range(n + 1)]

    # Add edges to the graph based on the given train lines
    for line in train_lines:
        graph[line[0]].append(line[1])
        graph[line[1]].append(line[0])

    # Find all possible routes with the minimum number of flights
    routes = []
    for city in range(1, n + 1):
        routes.extend(find_routes(graph, city, set(), []))

    # Print the minimum number of flights and the cities with airports that can be visited
    print(1)
    print(" ".join(str(route[0]) for route in routes))

def find_routes(graph, city, visited, route):
    # If all cities have been visited, return the current route
    if len(visited) == len(graph):
        return [route]

    # If the current city has already been visited, return an empty list
    if city in visited:
        return []

    # Mark the current city as visited and add it to the route
    visited.add(city)
    route.append(city)

    # Recursively find all possible routes from the current city
    routes = []
    for neighbor in graph[city]:
        routes.extend(find_routes(graph, neighbor, visited, route))

    # If no routes were found, return the current route
    if not routes:
        return [route]

    # Return all possible routes
    return routes

