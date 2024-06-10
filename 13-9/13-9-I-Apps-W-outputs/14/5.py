
def get_bus_route(intersections, roads):
    # Initialize a graph with the given intersections and roads
    graph = {}
    for intersection in intersections:
        graph[intersection] = []
    for road in roads:
        graph[road[0]].append((road[1], road[2]))
        graph[road[1]].append((road[0], road[2]))

    # Find a path from Delft (intersection 0) to Amsterdam (intersection 1)
    path = []
    queue = [(0, [0])]
    while queue:
        (current_intersection, current_path) = queue.pop(0)
        if current_intersection == 1:
            path = current_path
            break
        for next_intersection, distance in graph[current_intersection]:
            if next_intersection not in current_path:
                queue.append((next_intersection, current_path + [next_intersection]))

    # Check if the path satisfies the requirement
    if len(path) == 0:
        return "impossible"
    for i in range(len(path) - 1):
        intersection1 = path[i]
        intersection2 = path[i + 1]
        distance = 0
        for road in roads:
            if (road[0] == intersection1 and road[1] == intersection2) or (road[0] == intersection2 and road[1] == intersection1):
                distance = road[2]
                break
        if distance != 0:
            return "impossible"

    # Return the path if it satisfies the requirement
    return len(path), path

def main():
    # Read input from stdin
    n, m = map(int, input().split())
    roads = []
    for _ in range(m):
        a, b, d = map(int, input().split())
        roads.append((a, b, d))

    # Call the function to get the bus route
    result = get_bus_route(range(n), roads)

    # Print the result
    if result == "impossible":
        print("impossible")
    else:
        print(result[0])
        for i in result[1]:
            print(i, end=" ")
        print()

if __name__ == '__main__':
    main()

