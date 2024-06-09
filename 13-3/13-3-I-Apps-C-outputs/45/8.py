
def solve(n, m, s, edges):
    # Initialize the graph as an adjacency list
    graph = [[] for _ in range(n + 1)]
    for edge in edges:
        graph[edge[1]].append(edge[2])
        graph[edge[2]].append(edge[1])

    # Find all reachable vertices from vertex s
    reachable = set([s])
    queue = [s]
    while queue:
        vertex = queue.pop(0)
        for neighbor in graph[vertex]:
            if neighbor not in reachable:
                reachable.add(neighbor)
                queue.append(neighbor)

    # Initialize the plans
    plan1 = []
    plan2 = []

    # Iterate through the edges and add them to the plans
    for edge in edges:
        if edge[0] == 1:  # directed edge
            plan1.append(edge)
            plan2.append(edge)
        else:  # undirected edge
            plan1.append((edge[0], edge[1], edge[2], 1))
            plan1.append((edge[0], edge[2], edge[1], -1))
            plan2.append((edge[0], edge[1], edge[2], -1))
            plan2.append((edge[0], edge[2], edge[1], 1))

    # Return the plans
    return (len(reachable), "".join([str(edge[3]) for edge in plan1]), len(reachable), "".join([str(edge[3]) for edge in plan2]))

