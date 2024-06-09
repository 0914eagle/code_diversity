
def solve():
    import sys
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    heights = data[2:(2 * n + 2):2]
    roads = list(zip(data[(2 * n + 2):(2 * n + 2 + m * 2):2], data[(3 * n + 4):(2 * n + 2 + m * 2):2]))

    # Create a graph with the roads as edges
    graph = [[] for _ in range(n)]
    for road in roads:
        graph[road[0] - 1].append(road[1] - 1)

    # Find the good observatories by starting from each observatory and checking if it is higher than all the observatories it can reach
    good_observatories = 0
    for i in range(n):
        visited = [False] * n
        queue = [i]
        visited[i] = True
        while queue:
            observatory = queue.pop(0)
            for neighbor in graph[observatory]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
        if visited.count(True) == 1:
            good_observatories += 1

    return good_observatories

