
def solve(N, towns):
    # Sort the towns by their x-coordinates
    sorted_towns = sorted(towns, key=lambda town: town[0])

    # Create a graph with an edge between each pair of towns
    graph = {}
    for i in range(N):
        graph[i] = []

    for i in range(N-1):
        for j in range(i+1, N):
            graph[i].append(j)
            graph[j].append(i)

    # Calculate the minimum spanning tree using Kruskal's algorithm
    mst = []
    visited = set()
    while graph:
        # Find the edge with the minimum weight
        min_weight = float('inf')
        min_edge = None
        for i in graph:
            for j in graph[i]:
                if j not in visited:
                    weight = abs(sorted_towns[i][0] - sorted_towns[j][0])
                    if weight < min_weight:
                        min_weight = weight
                        min_edge = (i, j)

        # Add the edge to the MST
        mst.append(min_edge)
        visited.add(min_edge[1])
        graph[min_edge[0]].remove(min_edge[1])
        if not graph[min_edge[0]]:
            del graph[min_edge[0]]

    # Calculate the total cost of the MST
    total_cost = 0
    for edge in mst:
        town1 = sorted_towns[edge[0]]
        town2 = sorted_towns[edge[1]]
        total_cost += abs(town1[0] - town2[0])

    return total_cost

