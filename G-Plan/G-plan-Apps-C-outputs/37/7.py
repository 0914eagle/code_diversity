_earliest_start_time(N, M, trains):
    def calculate_delay(departure, arrival, delay):
        return max(0, arrival - departure - delay)

    sorted_trains = sorted(trains, key=lambda x: x[1])
    earliest_start_time = float('inf')

    for i in range(M):
        current_start_time = sorted_trains[i][1]
        current_end_time = sorted_trains[i][2]
        current_delay = sorted_trains[i][3]

        if i == 0:
            earliest_start_time = min(earliest_start_time, current_start_time - calculate_delay(0, current_start_time, 0))
        else:
            prev_end_time = sorted_trains[i - 1][2]
            prev_delay = sorted_trains[i - 1][3]
            earliest_start_time = min(earliest_start_time, current_start_time - calculate_delay(prev_end_time, current_start_time, prev_delay))

    return earliest_start_time if earliest_start_time != float('inf') else "impossible"

if __name__ == "__main__":
    N, M = map(int, input().split())
    trains = [list(map(int, input().split())) for _ in range(M)]

    result = find_earliest_start_time(N, M, trains)
    print(result)
""