
def is_k_multihedgehog(graph, k):
    # Check if the graph is a tree
    if not is_tree(graph):
        return False

    # Check if the graph has at least one vertex with degree at least 3
    center = None
    for vertex in graph:
        if graph.degree[vertex] >= 3:
            center = vertex
            break
    if center is None:
        return False

    # Check if all other vertices have degree 1
    for vertex in graph:
        if vertex != center and graph.degree[vertex] != 1:
            return False

    # Check if the graph is a k-multihedgehog
    for vertex in graph:
        if vertex == center:
            continue
        neighbor = graph.neighbors(vertex)[0]
        if not is_k_multihedgehog_helper(graph, neighbor, center, k-1):
            return False

    return True

def is_k_multihedgehog_helper(graph, vertex, center, k):
    if k == 0:
        return True
    if graph.degree[vertex] != 1:
        return False
    neighbor = graph.neighbors(vertex)[0]
    if neighbor == center:
        return False
    return is_k_multihedgehog_helper(graph, neighbor, center, k-1)

def is_tree(graph):
    # Check if the graph is connected
    if not is_connected(graph):
        return False

    # Check if the graph is a tree
    visited = set()
    to_visit = [0]
    while to_visit:
        vertex = to_visit.pop()
        if vertex in visited:
            continue
        visited.add(vertex)
        for neighbor in graph.neighbors(vertex):
            if neighbor not in visited:
                to_visit.append(neighbor)

    return len(visited) == graph.order()

def is_connected(graph):
    # Check if the graph is connected
    visited = set()
    to_visit = [0]
    while to_visit:
        vertex = to_visit.pop()
        if vertex in visited:
            continue
        visited.add(vertex)
        for neighbor in graph.neighbors(vertex):
            if neighbor not in visited:
                to_visit.append(neighbor)

    return len(visited) == graph.order()

