
def get_input():
    N, M = map(int, input().split())
    translators = []
    for _ in range(M):
        translator = list(map(int, input().split()))
        translators.append(translator)
    return N, M, translators

def is_bipartite(graph):
    visited = [False] * len(graph)
    color = [False] * len(graph)
    for i in range(len(graph)):
        if not visited[i]:
            if not dfs(graph, i, visited, color):
                return False
    return True

def dfs(graph, node, visited, color):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            color[neighbor] = not color[node]
            if not dfs(graph, neighbor, visited, color):
                return False
        elif color[neighbor] == color[node]:
            return False
    return True

def solve(N, M, translators):
    graph = [[] for _ in range(N)]
    for translator in translators:
        graph[translator[0]].append(translator[1])
        graph[translator[1]].append(translator[0])
    if is_bipartite(graph):
        return "impossible"
    matching = []
    for i in range(N):
        for j in range(i+1, N):
            if graph[i][j]:
                matching.append([i, j])
    return matching

def main():
    N, M, translators = get_input()
    print(solve(N, M, translators))

if __name__ == '__main__':
    main()

