
def f1(n, m, rap_battles):
    # Initialize a graph with n vertices and no edges
    graph = [[] for _ in range(n)]

    # Add edges to the graph based on the rap battles
    for u, v in rap_battles:
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)

    # Find the strongly connected components in the graph
    scc = strongly_connected_components(graph)

    # Return the minimum number of rap battles needed to determine the ordering of the robots
    return m - len(scc)

def f2(n, m, rap_battles):
    # Initialize a graph with n vertices and no edges
    graph = [[] for _ in range(n)]

    # Add edges to the graph based on the rap battles
    for u, v in rap_battles:
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)

    # Find the strongly connected components in the graph
    scc = strongly_connected_components(graph)

    # If there is more than one SCC, return -1
    if len(scc) > 1:
        return -1

    # Otherwise, return the minimum number of rap battles needed to determine the ordering of the robots
    return m - len(scc[0])

def strongly_connected_components(graph):
    # Initialize a list to store the strongly connected components
    scc = []

    # Initialize a queue to do a breadth-first search of the graph
    queue = [0]

    # Loop until the queue is empty
    while queue:
        # Dequeue a vertex from the queue
        u = queue.pop(0)

        # If the vertex has not been visited yet, mark it as visited and add it to the current SCC
        if u not in visited:
            visited.add(u)
            scc[-1].append(u)

            # Enqueue the neighbors of the vertex
            for v in graph[u]:
                if v not in visited:
                    queue.append(v)

    # Return the list of strongly connected components
    return scc

if __name__ == '__main__':
    n, m = map(int, input().split())
    rap_battles = []
    for _ in range(m):
        u, v = map(int, input().split())
        rap_battles.append((u, v))
    print(f1(n, m, rap_battles))
    print(f2(n, m, rap_battles))
