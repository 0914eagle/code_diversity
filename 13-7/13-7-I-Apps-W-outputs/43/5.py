
def get_graph(n, k):
    # f is an array containing the number of vertex to which goes the only arc from the vertex i
    f = list(map(int, input().split()))
    # w is an array containing the weight of the arcs from i to f[i]
    w = list(map(int, input().split()))
    
    # Initialize the graph as a dictionary, where each key is a vertex and the value is a list of tuples (neighbor, weight)
    graph = {i: [] for i in range(n)}
    for i in range(n):
        graph[i].append((f[i], w[i]))
    
    return graph

def get_path(graph, k):
    # Initialize the sum of the weights of all arcs of the path with length equals to k which starts from the vertex i as 0
    s = 0
    # Initialize the minimal weight from all arcs on the path with length k which starts from the vertex i as infinity
    m = float('inf')
    
    # Iterate through all vertices in the graph
    for i in range(len(graph)):
        # If the current vertex is not the last vertex in the path, add the weight of the arc from the current vertex to its neighbor to the sum of the weights
        if i != len(graph) - 1:
            s += graph[i][0][1]
        # If the current vertex is the last vertex in the path, set the minimal weight to the weight of the arc from the current vertex to its neighbor
        else:
            m = graph[i][0][1]
        
        # If the length of the path is greater than 1, recursively call the function for the neighbor of the current vertex with the length of the path minus 1
        if len(graph) > 1:
            s, m = get_path(graph[i][0][0], k - 1)
        
        # Return the sum of the weights and the minimal weight of the path
        return s, m

def main():
    # Read the input data
    n, k = map(int, input().split())
    graph = get_graph(n, k)
    
    # Call the function to get the sum of the weights and the minimal weight of the path for each vertex
    for i in range(n):
        s, m = get_path(graph, k)
        print(s, m)

if __name__ == '__main__':
    main()

