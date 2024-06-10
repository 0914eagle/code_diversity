
def find_min_unable_teams(N, S, R, damaged_teams, reserve_teams):
    teams = [0] * (N + 1)
    for team in damaged_teams:
        teams[team] = -1
    for team in reserve_teams:
        teams[team] = 1

    unable_teams = 0
    for i in range(1, N + 1):
        if teams[i] == -1:
            if i > 1 and teams[i - 1] == 1:
                teams[i] = 1
                teams[i - 1] = 0
            elif i < N and teams[i + 1] == 1:
                teams[i] = 1
                teams[i + 1] = 0
            else:
                unable_teams += 1

    return unable_teams

if __name__ == "__main__":
    N, S, R = map(int, input().split())
    damaged_teams = list(map(int, input().split()))
    reserve_teams = list(map(int, input().split()))

    result = find_min_unable_teams(N, S, R, damaged_teams, reserve_teams)
    print(result)
