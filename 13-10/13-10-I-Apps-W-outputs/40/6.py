
def get_maximum_dominoes(n, m, edges):
    # Initialize a dictionary to store the number of dominoes that can be placed on each vertex
    vertex_dominoes = {i: 0 for i in range(1, n + 1)}

    # Iterate over the edges and increment the number of dominoes that can be placed on each vertex
    for edge in edges:
        vertex_dominoes[edge[0]] += 1
        vertex_dominoes[edge[1]] += 1

    # Initialize a set to store the maximum number of dominoes that can be placed on the edges
    max_dominoes = set()

    # Iterate over the vertices and find the maximum number of dominoes that can be placed on the edges incident to each vertex
    for vertex in vertex_dominoes:
        max_dominoes.add(vertex_dominoes[vertex])

    return max(max_dominoes)

def main():
    n, m = map(int, input().split())
    edges = []
    for i in range(m):
        edges.append(list(map(int, input().split())))
    print(get_maximum_dominoes(n, m, edges))

if __name__ == '__main__':
    main()

