
def solve(N, towns):
    # Sort the towns by their x-coordinates
    sorted_towns = sorted(towns, key=lambda town: town[0])

    # Create a graph with an edge between each pair of towns
    graph = {}
    for i in range(N):
        graph[i] = []

    for i in range(N-1):
        graph[i].append(i+1)

    # Calculate the minimum cost of building a road between each pair of towns
    min_cost = 0
    for i in range(N-1):
        for j in range(i+1, N):
            town1, town2 = sorted_towns[i], sorted_towns[j]
            cost = abs(town1[0] - town2[0]) + abs(town1[1] - town2[1])
            min_cost += cost

    return min_cost

