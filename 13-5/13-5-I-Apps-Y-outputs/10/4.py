
def get_input():
    n = int(input())
    edges = []
    for i in range(n - 1):
        edges.append(list(map(int, input().split())))
    return n, edges

def find_maximum_edges(n, edges):
    # Initialize a dictionary to store the number of edges for each vertex
    num_edges = {i: 0 for i in range(1, n + 1)}
    
    # Iterate over the edges and increment the number of edges for each vertex
    for edge in edges:
        num_edges[edge[0]] += 1
        num_edges[edge[1]] += 1
    
    # Find the vertex with the maximum number of edges
    max_vertex = max(num_edges, key=num_edges.get)
    
    # Find the two vertices that are not adjacent to the maximum vertex
    non_adjacent_vertices = []
    for i in range(1, n + 1):
        if i != max_vertex and (max_vertex, i) not in edges and (i, max_vertex) not in edges:
            non_adjacent_vertices.append(i)
    
    # Find the vertex that is adjacent to both the maximum vertex and one of the non-adjacent vertices
    third_vertex = -1
    for edge in edges:
        if edge[0] == max_vertex and edge[1] in non_adjacent_vertices:
            third_vertex = edge[1]
            break
        elif edge[1] == max_vertex and edge[0] in non_adjacent_vertices:
            third_vertex = edge[0]
            break
    
    # Find the maximum number of edges that are part of at least one of the simple paths between the three vertices
    max_edges = 0
    for edge in edges:
        if edge[0] == max_vertex or edge[1] == max_vertex or (edge[0] == third_vertex and edge[1] in non_adjacent_vertices) or (edge[1] == third_vertex and edge[0] in non_adjacent_vertices):
            max_edges += 1
    
    return max_edges, max_vertex, third_vertex

def main():
    n, edges = get_input()
    max_edges, max_vertex, third_vertex = find_maximum_edges(n, edges)
    print(max_edges)
    print(max_vertex, third_vertex)

if __name__ == '__main__':
    main()

