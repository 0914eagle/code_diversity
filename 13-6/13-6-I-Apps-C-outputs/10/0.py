
def is_k_multihedgehog(graph, k):
    # Check if the graph is a tree
    if not is_tree(graph):
        return False

    # Check if the graph has at least one vertex with degree at least 3
    center = None
    for node in graph:
        if graph.degree(node) >= 3:
            center = node
            break
    if center is None:
        return False

    # Check if all other vertices have degree 1
    for node in graph:
        if node != center and graph.degree(node) != 1:
            return False

    # Check if the graph is a k-multihedgehog
    for i in range(k-1):
        # Find the vertex with degree 1
        vertex = None
        for node in graph:
            if graph.degree(node) == 1:
                vertex = node
                break
        if vertex is None:
            return False

        # Find the neighbor of the vertex with degree 1
        neighbor = None
        for node in graph:
            if node != vertex and graph.has_edge(node, vertex):
                neighbor = node
                break
        if neighbor is None:
            return False

        # Create a new hedgehog with center at the vertex with degree 1
        new_graph = Graph()
        new_graph.add_node(vertex)
        new_graph.add_node(neighbor)
        new_graph.add_edge(vertex, neighbor)

        # Add the new hedgehog to the graph
        graph.merge(new_graph)

    # Check if the graph is still a tree
    if not is_tree(graph):
        return False

    # Check if the graph has at least one vertex with degree at least 3
    center = None
    for node in graph:
        if graph.degree(node) >= 3:
            center = node
            break
    if center is None:
        return False

    # Check if all other vertices have degree 1
    for node in graph:
        if node != center and graph.degree(node) != 1:
            return False

    return True

def is_tree(graph):
    # Check if the graph is connected
    if not is_connected(graph):
        return False

    # Check if the graph has no cycles
    for node in graph:
        if has_cycle(graph, node):
            return False

    return True

def is_connected(graph):
    # Check if the graph is connected by doing a BFS from an arbitrary node
    node = next(iter(graph))
    visited = set()
    queue = [node]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            queue.extend(graph.neighbors(node))

    return len(visited) == len(graph)

def has_cycle(graph, node):
    # Check if the graph has a cycle by doing a DFS from the node
    visited = set()
    stack = [node]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            stack.extend(graph.neighbors(node))
        else:
            return True

    return False

