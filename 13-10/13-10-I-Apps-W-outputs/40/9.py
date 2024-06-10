
def get_max_dominoes(n, m, edges):
    # Initialize a dictionary to store the number of dominoes that can be placed on each vertex
    vertex_dominoes = {}
    for i in range(1, n + 1):
        vertex_dominoes[i] = 0

    # Iterate over the edges and update the dictionary
    for edge in edges:
        vertex1, vertex2 = edge[0], edge[1]
        vertex_dominoes[vertex1] += 1
        vertex_dominoes[vertex2] += 1

    # Find the vertex with the maximum number of dominoes
    max_dominoes = max(vertex_dominoes.values())

    # Return the maximum number of dominoes that can be placed on the edges
    return max_dominoes

def main():
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        edges.append(list(map(int, input().split())))
    print(get_max_dominoes(n, m, edges))

if __name__ == '__main__':
    main()

