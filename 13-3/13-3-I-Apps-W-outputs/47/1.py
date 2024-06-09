
def solve(N, towns):
    # Sort the towns by their x-coordinates
    towns.sort(key=lambda town: town[0])

    # Create a graph with an edge between each pair of towns
    graph = [[] for _ in range(N)]
    for i in range(N-1):
        for j in range(i+1, N):
            graph[i].append(j)

    # Calculate the minimum cost of connecting each pair of towns
    min_cost = 0
    for i in range(N-1):
        for j in range(i+1, N):
            min_cost += min(abs(towns[i][0] - towns[j][0]), abs(towns[i][1] - towns[j][1]))

    return min_cost

