
def find_min_unable_teams(N, S, R, damaged_teams, reserve_teams):
    graph = {i: [] for i in range(1, N + 1)}
    for team in reserve_teams:
        if team - 1 in graph:
            graph[team].append(team - 1)
        if team + 1 in graph:
            graph[team].append(team + 1)
    
    visited = set()
    
    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
    
    for team in reserve_teams:
        dfs(team)
    
    unable_teams = 0
    for team in range(1, N + 1):
        if team not in visited and team not in damaged_teams:
            unable_teams += 1
    
    return unable_teams

if __name__ == "__main__":
    N, S, R = map(int, input().split())
    damaged_teams = set(map(int, input().split()))
    reserve_teams = set(map(int, input().split()))
    
    result = find_min_unable_teams(N, S, R, damaged_teams, reserve_teams)
    print(result)
