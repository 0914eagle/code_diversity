
def minimal_time_required(N, teams):
    teams.sort(reverse=True)
    total_time = 0
    for i, time in enumerate(teams):
        if i % 2 == 0:
            total_time += time
    return total_time

if __name__ == "__main__":
    N = int(input())
    teams = list(map(int, input().split()))
    result = minimal_time_required(N, teams)
    print(result)
