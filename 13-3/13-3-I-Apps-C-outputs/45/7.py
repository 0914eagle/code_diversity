
def solve(n, m, s, edges):
    # Initialize the graph as an adjacency list
    graph = [[] for _ in range(n + 1)]
    for edge in edges:
        graph[edge[1]].append(edge[2])
        graph[edge[2]].append(edge[1])

    # Find all reachable vertices from the starting vertex
    reachable = [False] * (n + 1)
    queue = [s]
    while queue:
        vertex = queue.pop(0)
        if not reachable[vertex]:
            reachable[vertex] = True
            queue += graph[vertex]

    # Initialize the plans as empty lists
    plan1 = []
    plan2 = []

    # Iterate through the edges and add them to the plans
    for edge in edges:
        if edge[0] == 1:  # directed edge
            plan1.append(edge)
            plan2.append(edge)
        else:  # undirected edge
            if reachable[edge[1]] and reachable[edge[2]]:  # both vertices are reachable
                plan1.append(edge)
                plan2.append(edge)
            elif reachable[edge[1]]:  # only one vertex is reachable
                plan1.append((1, edge[1], edge[2]))
                plan2.append((1, edge[2], edge[1]))
            elif reachable[edge[2]]:
                plan1.append((1, edge[2], edge[1]))
                plan2.append((1, edge[1], edge[2]))
            else:  # neither vertex is reachable
                plan1.append((1, edge[1], edge[2]))
                plan2.append((1, edge[2], edge[1]))

    # Return the plans
    return plan1, plan2

