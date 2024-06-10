d_graph(N, cities):
    graph = {i: [] for i in range(N)}
    for i in range(N):
        for j in range(i + 1, N):
            dist = ((cities[i][0] - cities[j][0]) ** 2 + (cities[i][1] - cities[j][1]) ** 2) ** 0.5
            if dist <= D:
                graph[i].append(j)
                graph[j].append(i)
    return graph

def dfs(node, visited, graph, total_residents):
    visited[node] = True
    total_residents[0] += cities[node][2]
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(neighbor, visited, graph, total_residents)

def check_happiness(graph, cities, K):
    visited = [False] * len(cities)
    for i in range(len(cities)):
        if not visited[i]:
            total_residents = [0]
            dfs(i, visited, graph, total_residents)
            if total_residents[0] % K == 0:
                return True
    return False

def binary_search_minimal_D(N, cities, K):
    low, high = 0, 10**9
    while high - low > 1e-9:
        global D
        D = (low + high) / 2
        graph = build_graph(N, cities)
        if check_happiness(graph, cities, K):
            high = D
        else:
            low = D
    return D

if __name__ == "__main__":
    N, K = map(int, input().split())
    cities = [list(map(int, input().split())) for _ in range(N)]
    print("{:.3f}".format(binary_search_minimal_D(N, cities, K)))
