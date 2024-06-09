
def solve(N, towns):
    # Sort the towns by their x-coordinates
    sorted_towns = sorted(towns, key=lambda town: town[0])

    # Create a graph with an edge between each pair of towns
    graph = {}
    for i in range(N):
        graph[i] = []
        for j in range(i+1, N):
            graph[i].append(j)

    # Calculate the minimum cost of building a road between each pair of towns
    min_cost = 0
    for i in range(N):
        for j in graph[i]:
            min_cost += min(abs(sorted_towns[i][0] - sorted_towns[j][0]), abs(sorted_towns[i][1] - sorted_towns[j][1]))

    return min_cost

