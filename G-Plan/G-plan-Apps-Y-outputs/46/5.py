
def minimal_time_required(N, teams):
    teams.sort(reverse=True)
    total_time = 0
    for i, team_time in enumerate(teams):
        if i % 2 == 0:
            total_time += team_time
    return total_time

if __name__ == "__main__":
    N = int(input())
    teams = list(map(int, input().split()))
    print(minimal_time_required(N, teams))
