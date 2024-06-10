
def get_max_dominoes(n, m, edges):
    # Initialize a dictionary to store the number of dominoes that can be placed on each vertex
    vertex_dominoes = {}
    for i in range(1, n + 1):
        vertex_dominoes[i] = 0

    # Iterate over the edges and update the number of dominoes that can be placed on each vertex
    for edge in edges:
        vertex_dominoes[edge[0]] += 1
        vertex_dominoes[edge[1]] += 1

    # Initialize a variable to store the maximum number of dominoes that can be placed
    max_dominoes = 0

    # Iterate over the vertices and update the maximum number of dominoes that can be placed
    for vertex in vertex_dominoes:
        max_dominoes = max(max_dominoes, vertex_dominoes[vertex])

    return max_dominoes

def main():
    n, m = map(int, input().split())
    edges = []
    for i in range(m):
        edge = list(map(int, input().split()))
        edges.append(edge)
    print(get_max_dominoes(n, m, edges))

if __name__ == '__main__':
    main()

