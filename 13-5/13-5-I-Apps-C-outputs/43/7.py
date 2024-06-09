
import sys

sys.setrecursionlimit(10000)


def shortest_paths(n, roads):
    # Initialize the graph with the given roads
    graph = [[] for _ in range(n + 1)]
    for o, d, l in roads:
        graph[o].append((d, l))

    # Initialize the number of shortest paths for each road
    num_shortest_paths = [0] * len(roads)

    # Function to find the shortest path from city 1 to city n
    def find_shortest_path(city, visited, path_length):
        nonlocal num_shortest_paths

        # If we have visited all cities, update the number of shortest paths
        if city == n:
            num_shortest_paths[path_length] += 1
            return

        # Iterate over all the roads from the current city
        for next_city, length in graph[city]:
            # If we have already visited the next city, skip it
            if next_city in visited:
                continue

            # Add the length of the road to the path length
            new_path_length = path_length + length

            # If the new path length is greater than the number of cities, skip it
            if new_path_length > n:
                continue

            # Mark the next city as visited and recurse
            visited.add(next_city)
            find_shortest_path(next_city, visited, new_path_length)

            # Remove the next city from the visited set
            visited.remove(next_city)

    # Find the shortest path from city 1 to city n
    find_shortest_path(1, set(), 0)

    # Return the number of shortest paths for each road
    return num_shortest_paths


n, m = map(int, input().split())
roads = []
for _ in range(m):
    o, d, l = map(int, input().split())
    roads.append((o, d, l))

num_shortest_paths = shortest_paths(n, roads)
print(*num_shortest_paths, sep="\n")

