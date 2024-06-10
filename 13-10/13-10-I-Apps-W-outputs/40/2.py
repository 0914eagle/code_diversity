
def get_maximum_dominoes(n, m, edges):
    # Initialize a dictionary to store the number of dominoes that can be placed on each vertex
    dominoes_on_vertex = {}
    for i in range(1, n + 1):
        dominoes_on_vertex[i] = 0
    
    # Iterate through the edges and increment the number of dominoes that can be placed on each vertex
    for edge in edges:
        vertex1, vertex2 = edge[0], edge[1]
        dominoes_on_vertex[vertex1] += 1
        dominoes_on_vertex[vertex2] += 1
    
    # Initialize a variable to store the maximum number of dominoes that can be placed on the edges
    maximum_dominoes = 0
    
    # Iterate through the dictionary and find the maximum number of dominoes that can be placed on the edges
    for vertex, dominoes in dominoes_on_vertex.items():
        maximum_dominoes = max(maximum_dominoes, dominoes)
    
    return maximum_dominoes

def main():
    n, m = map(int, input().split())
    edges = []
    for i in range(m):
        edge = list(map(int, input().split()))
        edges.append(edge)
    print(get_maximum_dominoes(n, m, edges))

if __name__ == '__main__':
    main()

