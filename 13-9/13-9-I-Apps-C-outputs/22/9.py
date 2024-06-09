
def solve(n, points):
    # Sort the points by their x-coordinate
    sorted_points = sorted(points, key=lambda x: x[0])

    # Create a graph with the points as vertices and edges between adjacent points
    graph = {}
    for i in range(n):
        graph[i] = [i+1]

    # Iterate through the points and add edges between adjacent points
    for i in range(n-1):
        graph[i].append(i+2)

    # Check if the graph is a tree
    if not is_tree(graph):
        return "NO"

    # Check if the loop goes through all points
    if not goes_through_all_points(graph, sorted_points):
        return "NO"

    # Check if the loop is a single loop
    if not is_single_loop(graph):
        return "NO"

    return "YES"

def is_tree(graph):
    # Check if the graph is a tree by performing a depth-first search
    visited = set()
    stack = [0]
    while stack:
        node = stack.pop()
        if node in visited:
            return False
        visited.add(node)
        stack.extend(graph[node])
    return True

def goes_through_all_points(graph, sorted_points):
    # Check if the loop goes through all points
    visited = set()
    current_node = 0
    while len(visited) < len(sorted_points):
        next_node = graph[current_node][0]
        if next_node not in visited:
            visited.add(next_node)
            current_node = next_node
        else:
            return False
    return True

def is_single_loop(graph):
    # Check if the loop is a single loop by checking if all edges are used exactly once
    used_edges = set()
    for node in graph:
        for neighbor in graph[node]:
            if (node, neighbor) in used_edges or (neighbor, node) in used_edges:
                return False
            used_edges.add((node, neighbor))
    return True

n = int(input())
points = []
for i in range(n):
    x, y = map(int, input().split())
    points.append((x, y))
print(solve(n, points))

