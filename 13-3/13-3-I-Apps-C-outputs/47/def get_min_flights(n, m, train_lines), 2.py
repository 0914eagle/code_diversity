
def get_min_flights(n, m, train_lines):
    # Initialize a graph with the train lines
    graph = [[] for i in range(n + 1)]
    for i in range(m):
        graph[train_lines[i][0]].append(train_lines[i][1])
        graph[train_lines[i][1]].append(train_lines[i][0])

    # Find all possible routes with the minimum number of flights
    min_flights = 1
    routes = []
    for i in range(1, n + 1):
        route = [i]
        visited = [False] * (n + 1)
        visited[i] = True
        get_routes_recursive(graph, route, visited, min_flights, routes)

    # Find the airports that can be visited on any of the routes with the minimum number of flights
    airports = []
    for route in routes:
        for i in range(1, n + 1):
            if i in route and i % 2 == 0:
                airports.append(i)
                break

    return [min_flights, " ".join([str(airport) for airport in airports])]

def get_routes_recursive(graph, route, visited, min_flights, routes):
    if len(route) == len(graph):
        routes.append(route[:])
        return

    for i in range(1, len(graph)):
        if not visited[i]:
            visited[i] = True
            route.append(i)
            get_routes_recursive(graph, route, visited, min_flights, routes)
            route.pop()
            visited[i] = False

if __name__ == "__main__":
    n, m = map(int, input().split())
    train_lines = []
    for i in range(m):
        a, b = map(int, input().split())
        train_lines.append([a, b])
    print(*get_min_flights(n, m, train_lines))

