
def minimal_time_for_lectures(N, teams_time):
    teams_time.sort(reverse=True)
    total_time = 0
    for i in range(N):
        if i % 2 == 0:
            total_time += teams_time[i]
    return total_time

if __name__ == "__main__":
    N = int(input())
    teams_time = list(map(int, input().split()))
    result = minimal_time_for_lectures(N, teams_time)
    print(result)
