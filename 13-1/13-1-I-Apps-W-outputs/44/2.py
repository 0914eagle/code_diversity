
def f1(n, m, rap_battles):
    # Initialize a graph with n vertices and no edges
    graph = [[] for _ in range(n)]

    # Add edges to the graph based on the rap battles
    for u, v in rap_battles:
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)

    # Find the strongly connected components in the graph
    scc = strongly_connected_components(graph)

    # If there is only one strongly connected component, then the ordering is unique
    if len(scc) == 1:
        return len(scc[0])
    else:
        return -1

def strongly_connected_components(graph):
    # Initialize a list to store the strongly connected components
    scc = []

    # Iterate through the vertices in the graph
    for v in range(len(graph)):
        # If the vertex has not been visited yet, then explore it
        if v not in visited:
            explore(v, graph, scc)

    return scc

def explore(v, graph, scc):
    # Mark the vertex as visited
    visited.add(v)

    # Add the vertex to the current strongly connected component
    scc[-1].append(v)

    # Iterate through the neighbors of the vertex
    for u in graph[v]:
        # If the neighbor has not been visited yet, then explore it
        if u not in visited:
            explore(u, graph, scc)

if __name__ == '__main__':
    n, m = map(int, input().split())
    rap_battles = []
    for _ in range(m):
        u, v = map(int, input().split())
        rap_battles.append((u, v))
    print(f1(n, m, rap_battles))

