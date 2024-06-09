
def get_input():
    n = int(input())
    edges = []
    for i in range(n - 1):
        edges.append(tuple(map(int, input().split())))
    return n, edges

def find_max_edges(n, edges):
    # Initialize a dictionary to store the number of edges for each vertex
    num_edges = {i: 0 for i in range(1, n + 1)}
    
    # Iterate over the edges and increment the number of edges for each vertex
    for edge in edges:
        num_edges[edge[0]] += 1
        num_edges[edge[1]] += 1
    
    # Find the vertex with the maximum number of edges
    max_vertex = max(num_edges, key=num_edges.get)
    
    # Find the two vertices that are not adjacent to the maximum vertex
    non_adjacent_vertices = [i for i in range(1, n + 1) if i != max_vertex and (max_vertex, i) not in edges]
    
    # Find the vertex that is adjacent to both the maximum vertex and one of the non-adjacent vertices
    third_vertex = [i for i in non_adjacent_vertices if (max_vertex, i) in edges][0]
    
    # Return the maximum number of edges and the three vertices
    return num_edges[max_vertex], [max_vertex, non_adjacent_vertices[0], third_vertex]

def main():
    n, edges = get_input()
    max_edges, vertices = find_max_edges(n, edges)
    print(max_edges)
    print(" ".join(map(str, vertices)))

if __name__ == '__main__':
    main()

