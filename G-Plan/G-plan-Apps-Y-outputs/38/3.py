
def find_min_unable_teams(N, S, R, damaged_teams, reserve_teams):
    teams = [0] * N
    for team in damaged_teams:
        teams[team - 1] = -1
    for team in reserve_teams:
        teams[team - 1] = 1

    unable_teams = 0
    for i in range(N):
        if teams[i] == -1:
            if i > 0 and teams[i - 1] == 1:
                teams[i] = 1
            elif i < N - 1 and teams[i + 1] == 1:
                teams[i] = 1
            else:
                unable_teams += 1

    return unable_teams

if __name__ == "__main__":
    N, S, R = map(int, input().split())
    damaged_teams = list(map(int, input().split()))
    reserve_teams = list(map(int, input().split()))

    result = find_min_unable_teams(N, S, R, damaged_teams, reserve_teams)
    print(result)
