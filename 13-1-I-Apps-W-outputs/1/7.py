
def solve(N, paths, order):
    # Initialize a graph with N nodes and 0 edges
    graph = [[] for _ in range(N)]

    # Add edges to the graph based on the given paths
    for path in paths:
        graph[path[0] - 1].append(path[1] - 1)
        graph[path[1] - 1].append(path[0] - 1)

    # Initialize a list to store the number of boring pairs before each destruction
    boring_pairs = [0]

    # Iterate through the order of destruction
    for i in range(1, len(order)):
        # Find the path that was destroyed in the previous step
        prev_path = order[i - 1]

        # Find the planets connected by the destroyed path
        planets = [paths[prev_path - 1][0], paths[prev_path - 1][1]]

        # Iterate through the remaining paths
        for j in range(len(paths)):
            # If the path is not the destroyed path and it connects one of the planets, remove it from the graph
            if j != prev_path - 1 and (paths[j][0] in planets or paths[j][1] in planets):
                graph[paths[j][0] - 1].remove(paths[j][1] - 1)
                graph[paths[j][1] - 1].remove(paths[j][0] - 1)

        # Count the number of boring pairs after the destruction
        boring_pairs.append(count_boring_pairs(graph, planets))

    return boring_pairs

def count_boring_pairs(graph, planets):
    # Initialize a counter for the number of boring pairs
    count = 0

    # Iterate through the planets
    for i in range(len(planets)):
        # Iterate through the neighbors of the current planet
        for j in range(len(graph[planets[i] - 1])):
            # If the neighbor is not one of the planets, it is a boring pair
            if graph[planets[i] - 1][j] not in planets:
                count += 1

    return count

