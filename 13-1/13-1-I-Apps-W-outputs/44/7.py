
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

    # Check if there is more than one ordering of the robots that satisfies all m relations
    if len(scc) == 1:
        return -1

    # Return the minimum number of rap battles needed to determine the ordering of the robots
    return m - len(scc) + 1

def strongly_connected_components(graph):
    # Initialize a queue to store the vertices to visit
    queue = []

    # Initialize a set to store the visited vertices
    visited = set()

    # Add the first vertex to the queue
    queue.append(0)

    # Loop until the queue is empty
    while queue:
        # Get the current vertex from the queue
        vertex = queue.pop(0)

        # If the current vertex has not been visited, mark it as visited and add it to the set
        if vertex not in visited:
            visited.add(vertex)

            # Add the neighbors of the current vertex to the queue
            for neighbor in graph[vertex]:
                queue.append(neighbor)

    # Return the set of visited vertices
    return visited

if __name__ == '__main__':
    n, m = map(int, input().split())
    rap_battles = []
    for _ in range(m):
        u, v = map(int, input().split())
        rap_battles.append((u, v))
    print(f1(n, m, rap_battles))
    print(f2(n, m, rap_battles))

