
def get_input():
    n = int(input())
    edges = []
    for i in range(n - 1):
        edges.append(list(map(int, input().split())))
    return n, edges

def find_maximum_edges(n, edges):
    # Initialize a dictionary to store the edges for each vertex
    vertex_edges = {i: set() for i in range(1, n + 1)}
    # Add the edges to the dictionary
    for edge in edges:
        vertex_edges[edge[0]].add(edge[1])
        vertex_edges[edge[1]].add(edge[0])
    # Initialize the maximum number of edges and the chosen vertices
    max_edges = 0
    a, b, c = 0, 0, 0
    # Iterate over all possible combinations of vertices
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            for k in range(j + 1, n + 1):
                # If the union of the paths between i, j, and k has more edges than the current maximum, update the maximum and the chosen vertices
                if len(vertex_edges[i] | vertex_edges[j] | vertex_edges[k]) > max_edges:
                    max_edges = len(vertex_edges[i] | vertex_edges[j] | vertex_edges[k])
                    a, b, c = i, j, k
    return max_edges, a, b, c

def print_output(max_edges, a, b, c):
    print(max_edges)
    print(a, b, c)

if __name__ == '__main__':
    n, edges = get_input()
    max_edges, a, b, c = find_maximum_edges(n, edges)
    print_output(max_edges, a, b, c)

