
def solve(n, edges):
    # Initialize a graph with n vertices and no edges
    graph = [[] for _ in range(n)]

    # Add edges to the graph
    for edge in edges:
        graph[edge[0] - 1].append(edge[1])
        graph[edge[1] - 1].append(edge[0])

    # Find the centroid of the graph
    centroid = find_centroid(graph)

    # Cut the edge between the centroid and any other vertex
    cut_edge = [centroid, 0]
    for i in range(1, n):
        if graph[centroid][i - 1] != 0:
            cut_edge[1] = i
            break

    # Add the edge between the centroid and any other vertex
    add_edge = [centroid, 0]
    for i in range(1, n):
        if graph[centroid][i - 1] == 0:
            add_edge[1] = i
            break

    return [cut_edge, add_edge]

def find_centroid(graph):
    # Find the vertex with the smallest degree
    min_degree = float('inf')
    centroid = 0
    for i in range(len(graph)):
        degree = len(graph[i])
        if degree < min_degree:
            min_degree = degree
            centroid = i

    return centroid

def main():
    tests = int(input())
    for _ in range(tests):
        n = int(input())
        edges = []
        for _ in range(n - 1):
            edges.append(list(map(int, input().split())))
        result = solve(n, edges)
        print(" ".join(map(str, result[0])))
        print(" ".join(map(str, result[1])))

if __name__ == '__main__':
    main()

