
def construct_forest(V, degrees):
    # Initialize a graph with the given number of vertices and no edges
    graph = [[] for _ in range(V)]

    # Iterate through the degrees and add edges to the graph
    for i, degree in enumerate(degrees):
        for j in range(i+1, V):
            if degree > 0 and graph[i] and graph[j]:
                graph[i].append(j)
                graph[j].append(i)
                degree -= 1

    # Check if the graph is connected
    visited = [False] * V
    queue = [0]
    while queue:
        vertex = queue.pop(0)
        if not visited[vertex]:
            visited[vertex] = True
            queue += graph[vertex]

    # If the graph is connected, return the edges, otherwise return "IMPOSSIBLE"
    if all(visited):
        edges = []
        for i, degree in enumerate(degrees):
            for j in graph[i]:
                if j > i:
                    edges.append([i+1, j+1])
                    degree -= 1
                    if degree == 0:
                        break
        return "POSSIBLE\n" + "\n".join(str(edge[0]) + " " + str(edge[1]) for edge in edges)
    else:
        return "IMPOSSIBLE"

if __name__ == '__main__':
    V = int(input())
    degrees = list(map(int, input().split()))
    print(construct_forest(V, degrees))

