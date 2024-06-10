
def get_turns_to_show_correct(intersections, a, b):
    # Initialize a graph with the given intersections and their connections
    graph = {i: {"left": l, "right": r} for i, l, r in intersections}

    # Initialize a queue to perform BFS
    queue = [(a, 0)]

    # Initialize a set to keep track of visited nodes
    visited = set()

    # Perform BFS to find the shortest path from intersection a to intersection b
    while queue:
        current, distance = queue.pop(0)
        if current == b:
            return distance
        if current not in visited:
            visited.add(current)
            queue += [(graph[current]["left"], distance + 1), (graph[current]["right"], distance + 1)]

    # If BFS fails to find a path, return "indistinguishable"
    return "indistinguishable"

def get_turns_to_show_correct_with_gps(intersections, a, b):
    # Initialize a graph with the given intersections and their connections
    graph = {i: {"left": l, "right": r} for i, l, r in intersections}

    # Initialize a queue to perform BFS
    queue = [(a, 0)]

    # Initialize a set to keep track of visited nodes
    visited = set()

    # Perform BFS to find the shortest path from intersection a to intersection b
    while queue:
        current, distance = queue.pop(0)
        if current == b:
            return distance
        if current not in visited:
            visited.add(current)
            queue += [(graph[current]["left"], distance + 1), (graph[current]["right"], distance + 1)]

    # If BFS fails to find a path, return "indistinguishable"
    return "indistinguishable"

def main():
    n, a, b = map(int, input().split())
    intersections = []
    for _ in range(n):
        intersections.append(list(map(int, input().split())))
    print(get_turns_to_show_correct(intersections, a, b))

if __name__ == '__main__':
    main()

