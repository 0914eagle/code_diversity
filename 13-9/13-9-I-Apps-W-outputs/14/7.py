
def get_shortest_route(intersections, roads):
    # Initialize a dictionary to store the shortest distance from each intersection to Amsterdam
    distances = {0: 0}
    # Initialize a dictionary to store the previous intersection for each intersection
    previous = {0: None}

    # Loop through each intersection
    for i in range(1, len(intersections)):
        # Loop through each road
        for road in roads:
            # If the current intersection is the starting intersection of the road
            if road[0] == i:
                # If the destination intersection of the road is not in the dictionary or the current distance is shorter than the previous distance
                if distances.get(road[1]) is None or distances[road[1]] > distances[i] + road[2]:
                    # Update the dictionary with the new shortest distance and the previous intersection
                    distances[road[1]] = distances[i] + road[2]
                    previous[road[1]] = i

    # Find the shortest path from Delft to Amsterdam
    path = [1]
    current = 1
    while previous[current] is not None:
        path.append(previous[current])
        current = previous[current]

    # Return the shortest path
    return path[::-1]

def main():
    # Read the input
    n, m = map(int, input().split())
    roads = []
    for _ in range(m):
        roads.append(list(map(int, input().split())))

    # Get the shortest route
    route = get_shortest_route([i for i in range(n)], roads)

    # Print the output
    if len(route) == n:
        print("impossible")
    else:
        print(len(route), *route)

if __name__ == '__main__':
    main()

