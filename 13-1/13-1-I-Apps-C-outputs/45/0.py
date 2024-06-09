
def construct_forest(V, degrees):
    # Initialize a graph with the given number of vertices and no edges
    graph = [[] for _ in range(V)]

    # Iterate through the degrees and add edges to the graph
    for i, degree in enumerate(degrees):
        for j in range(i+1, V):
            if degree > 0 and len(graph[i]) < degree:
                graph[i].append(j)
                degree -= 1
            if degree == 0:
                break
        if degree > 0:
            return "IMPOSSIBLE"

    # Check if the graph is connected
    visited = set()
    queue = [0]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex])
    if len(visited) == V:
        return "POSSIBLE"
    else:
        return "IMPOSSIBLE"

def main():
    V, degrees = map(int, input().split())
    degrees = list(map(int, input().split()))
    print(construct_forest(V, degrees))

if __name__ == '__main__':
    main()

