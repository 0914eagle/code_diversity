
def solve(n, vertices):
    # Calculate the distance between each pair of vertices
    distances = {}
    for i in range(n):
        for j in range(i+1, n):
            x1, y1 = vertices[i]
            x2, y2 = vertices[j]
            distances[(i, j)] = distances[(j, i)] = ((x2-x1)**2 + (y2-y1)**2)**0.5

    # Create a graph with the vertices as nodes and the distances as edges
    graph = [[] for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            graph[i].append((j, distances[(i, j)]))
            graph[j].append((i, distances[(i, j)]))

    # Find the minimum spanning tree of the graph
    parent = [None] * n
    key = [float('inf')] * n
    key[0] = 0
    mst = []
    for i in range(n):
        min_vertex = -1
        for j in range(n):
            if key[j] < key[min_vertex] or min_vertex == -1:
                min_vertex = j
        mst.append((min_vertex, parent[min_vertex]))
        for neighbor, weight in graph[min_vertex]:
            if key[neighbor] > weight:
                key[neighbor] = weight
                parent[neighbor] = min_vertex

    # Calculate the maximum circumference of the convex hexagon
    max_circumference = 0
    for i in range(n):
        vertex1 = mst[i][0]
        vertex2 = mst[i][1]
        vertex3 = mst[(i+1)%n][0]
        vertex4 = mst[(i+1)%n][1]
        vertex5 = mst[(i+2)%n][0]
        vertex6 = mst[(i+2)%n][1]
        circumference = distances[(vertex1, vertex2)] + distances[(vertex2, vertex3)] + distances[(vertex3, vertex4)] + distances[(vertex4, vertex5)] + distances[(vertex5, vertex6)] + distances[(vertex6, vertex1)]
        max_circumference = max(max_circumference, circumference)

    return max_circumference

