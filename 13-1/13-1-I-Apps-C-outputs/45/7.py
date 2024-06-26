
def is_forest(graph):
    # Check if the graph is a forest
    # A forest is a graph with no cycles
    # A graph is a forest if all of its vertices have degree at most 1
    for vertex in graph:
        if vertex.degree > 1:
            return False
    return True

def construct_forest(num_vertices, degrees):
    # Construct a graph with the given number of vertices and degrees
    graph = []
    for i in range(num_vertices):
        graph.append(Vertex(i, degrees[i]))
    
    # Add edges between vertices with degree 2
    for i in range(num_vertices):
        for j in range(i+1, num_vertices):
            if graph[i].degree == 2 and graph[j].degree == 2:
                graph[i].add_neighbor(graph[j])
                graph[j].add_neighbor(graph[i])
    
    # Add edges between vertices with degree 1
    for i in range(num_vertices):
        for j in range(i+1, num_vertices):
            if graph[i].degree == 1 and graph[j].degree == 1:
                graph[i].add_neighbor(graph[j])
                graph[j].add_neighbor(graph[i])
    
    # Check if the graph is a forest
    if is_forest(graph):
        return graph
    else:
        return None

def main():
    num_vertices = int(input())
    degrees = list(map(int, input().split()))
    graph = construct_forest(num_vertices, degrees)
    if graph is None:
        print("IMPOSSIBLE")
    else:
        print("POSSIBLE")
        for vertex in graph:
            for neighbor in vertex.neighbors:
                print(vertex.id, neighbor.id)

if __name__ == '__main__':
    main()

