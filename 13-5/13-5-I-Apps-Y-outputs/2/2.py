
def is_bridge(graph, edge):
    # Check if the edge is a bridge by removing it and checking if the graph is still connected
    graph.remove_edge(edge)
    connected = is_connected(graph)
    graph.add_edge(edge)
    return not connected

def count_bridges(graph):
    bridges = 0
    for edge in graph.edges:
        if is_bridge(graph, edge):
            bridges += 1
    return bridges

def is_connected(graph):
    # Check if the graph is connected by checking if all vertices are reachable from the first vertex
    queue = [0]
    visited = set()
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph.neighbors(vertex))
    return len(visited) == graph.v

def main():
    n, m = map(int, input().split())
    graph = UndirectedGraph(n)
    for _ in range(m):
        a, b = map(int, input().split())
        graph.add_edge(a, b)
    print(count_bridges(graph))

if __name__ == '__main__':
    main()

