
def build_graph(N, damaged_teams, reserve_teams):
    graph = {i: [] for i in range(1, N + 1)}
    for team in reserve_teams:
        if team - 1 in graph:
            graph[team].append(team - 1)
        if team + 1 in graph:
            graph[team].append(team + 1)
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
    return len(damaged_teams) - len(visited.intersection(set(damaged_teams)))

if __name__ == "__main__":
    N, S, R = map(int, input().split())
    damaged_teams = list(map(int, input().split()))
    reserve_teams = list(map(int, input().split()))
    result = min_teams_cannot_start(N, damaged_teams, reserve_teams)
    print(result)
