
def min_teams_cannot_start(N, S, R, damaged_teams, reserve_teams):
    teams = [0] * N
    for team in damaged_teams:
        teams[team - 1] = -1
    for team in reserve_teams:
        teams[team - 1] = 1

    for i in range(N):
        if teams[i] == 1:
            if i > 0 and teams[i - 1] == -1:
                teams[i - 1] = 1
            if i < N - 1 and teams[i + 1] == -1:
                teams[i + 1] = 1

    return teams.count(0)


if __name__ == "__main__":
    N, S, R = map(int, input().split())
    damaged_teams = list(map(int, input().split()))
    reserve_teams = list(map(int, input().split()))

    result = min_teams_cannot_start(N, S, R, damaged_teams, reserve_teams)
    print(result)
