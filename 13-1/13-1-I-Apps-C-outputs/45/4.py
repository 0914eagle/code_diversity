
def is_forest(graph):
    # Check if the graph is connected
    if not is_connected(graph):
        return False
    
    # Check if the graph has any cycles
    if has_cycles(graph):
        return False
    
    # Check if the degrees of the vertices are correct
    for node in graph:
        if graph.degree(node) != graph.node[node]['degree']:
            return False
    
    return True

def construct_forest(num_vertices, degrees):
    # Create a graph with the given number of vertices and degrees
    graph = nx.Graph()
    graph.add_nodes_from(range(1, num_vertices+1))
    for node, degree in degrees.items():
        graph.node[node]['degree'] = degree
    
    # Add edges to the graph
    for node in graph:
        for neighbor in graph.neighbors(node):
            if graph.node[neighbor]['degree'] > 0:
                graph.add_edge(node, neighbor)
                graph.node[neighbor]['degree'] -= 1
    
    # Check if the graph is a forest
    if is_forest(graph):
        return graph
    else:
        return None

def is_connected(graph):
    # Check if the graph is connected by performing a BFS from an arbitrary node
    queue = [0]
    visited = set()
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            queue.extend(graph.neighbors(node))
    
    return len(visited) == graph.number_of_nodes()

def has_cycles(graph):
    # Check if the graph has any cycles by performing a DFS from an arbitrary node
    visited = set()
    def dfs(node):
        if node in visited:
            return True
        visited.add(node)
        for neighbor in graph.neighbors(node):
            if dfs(neighbor):
                return True
        return False
    
    for node in graph:
        if dfs(node):
            return True
    return False

if __name__ == '__main__':
    num_vertices = int(input())
    degrees = {i: int(input()) for i in range(1, num_vertices+1)}
    graph = construct_forest(num_vertices, degrees)
    if graph is None:
        print("IMPOSSIBLE")
    else:
        print("POSSIBLE")
        for edge in graph.edges:
            print(edge[0], edge[1])

