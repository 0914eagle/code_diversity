
def solve(n, edges):
    # Convert the list of edges into a graph
    graph = {i: set() for i in range(1, n + 1)}
    for i, j in edges:
        graph[i].add(j)
        graph[j].add(i)

    # Find all centroids in the graph
    centroids = []
    for i in range(1, n + 1):
        if len(graph[i]) == 1:
            centroids.append(i)

    # If there is only one centroid, return it
    if len(centroids) == 1:
        return centroids[0], None

    # If there are multiple centroids, find the one that is not connected to the other centroids
    for i in centroids:
        for j in centroids:
            if i != j and graph[i].intersection(graph[j]):
                break
        else:
            return i, None

    # If all centroids are connected, find the edge that connects two of them and return it
    for i in centroids:
        for j in graph[i]:
            if j in centroids:
                return None, (i, j)


