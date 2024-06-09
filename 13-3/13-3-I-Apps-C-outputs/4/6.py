
def get_minimum_lounges(n_airports, n_routes, routes):
    # Initialize a graph with the given number of airports
    graph = [[] for _ in range(n_airports)]

    # Add edges to the graph based on the given routes
    for route in routes:
        graph[route[0] - 1].append(route[1] - 1)
        graph[route[1] - 1].append(route[0] - 1)

    # Initialize a set to store the airports that have a lounge
    lounges = set()

    # Iterate through the graph and find the minimum number of lounges necessary to satisfy the requirements
    for airport in range(n_airports):
        if airport not in lounges:
            queue = [airport]
            while queue:
                current = queue.pop(0)
                if current not in lounges:
                    lounges.add(current)
                    queue += graph[current]

    return len(lounges)

def main():
    n_airports, n_routes = map(int, input().split())
    routes = []
    for _ in range(n_routes):
        routes.append(list(map(int, input().split())))
    print(get_minimum_lounges(n_airports, n_routes, routes))

if __name__ == '__main__':
    main()

