
def solve(N, paths, order):
    # Initialize a graph with N nodes and 0 edges
    graph = [[] for _ in range(N)]

    # Add edges to the graph based on the input paths
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
        # Iterate through the planets again
        for j in range(i + 1, len(planets)):
            # If the XOR of the curiosities of the paths between the two planets is 0, it is a boring pair
            if xor_curiosity(graph, planets[i], planets[j]) == 0:
                count += 1

    return count

def xor_curiosity(graph, planet1, planet2):
    # Initialize a set to store the curiosities of the paths between the two planets
    curiosities = set()

    # Iterate through the paths between the two planets
    for path in graph[planet1]:
        if path in graph[planet2]:
            curiosities.add(path + 1)

    # Return the XOR of the curiosities
    return sum(curiosities) ^ (sum(curiosities) - 1)

