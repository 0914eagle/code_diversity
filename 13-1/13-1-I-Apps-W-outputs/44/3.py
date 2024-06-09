
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
        return m

    # If there are multiple strongly connected components, then the ordering is not unique
    return -1

def f2(n, m, rap_battles):
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
        return m

    # If there are multiple strongly connected components, then the ordering is not unique
    return -1

def strongly_connected_components(graph):
    # Initialize a queue to do a breadth-first search of the graph
    queue = [(0, 0)]

    # Initialize a visited array to keep track of which vertices have been visited
    visited = [False] * len(graph)

    # Initialize a component array to keep track of which component each vertex belongs to
    component = [-1] * len(graph)

    # Initialize the component number
    component_num = 0

    while queue:
        # Dequeue a vertex from the queue
        vertex, component_id = queue.pop(0)

        # If the vertex has not been visited, mark it as visited and add it to the current component
        if not visited[vertex]:
            visited[vertex] = True
            component[vertex] = component_id

            # Add the vertex's neighbors to the queue
            for neighbor in graph[vertex]:
                if not visited[neighbor]:
                    queue.append((neighbor, component_id))

        # If the vertex has been visited and it is not in the current component, create a new component
        elif component[vertex] != component_id:
            component_num += 1
            component[vertex] = component_num

            # Add the vertex's neighbors to the queue
            for neighbor in graph[vertex]:
                if not visited[neighbor]:
                    queue.append((neighbor, component_num))

    # Return the strongly connected components
    return [component[i] for i in range(len(graph)) if component[i] != -1]

if __name__ == '__main__':
    n, m = map(int, input().split())
    rap_battles = []
    for _ in range(m):
        u, v = map(int, input().split())
        rap_battles.append((u, v))
    print(f1(n, m, rap_battles))
    print(f2(n, m, rap_battles))

