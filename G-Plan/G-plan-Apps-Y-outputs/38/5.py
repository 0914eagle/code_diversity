
def build_graph(N, damaged_teams, reserve_teams):
    graph = {i: [] for i in range(1, N + 1)}
    for team in reserve_teams:
        if team - 1 in graph:
            graph[team].append(team - 1)
        if team + 1 in graph:
            graph[team].append(team + 1)
    for team in damaged_teams:
        if team in graph:
            del graph[team]
    return graph

def dfs(graph, start, visited):
    visited.add(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

def min_teams_cannot_start(N, damaged_teams, reserve_teams):
    graph = build_graph(N, damaged_teams, reserve_teams)
    visited = set()
    for team in reserve_teams:
        if team not in visited:
            dfs(graph, team, visited)
    return N - len(visited)

if __name__ == "__main__":
    N, S, R = map(int, input().split())
    damaged_teams = list(map(int, input().split()))
    reserve_teams = list(map(int, input().split()))
    print(min_teams_cannot_start(N, damaged_teams, reserve_teams))
