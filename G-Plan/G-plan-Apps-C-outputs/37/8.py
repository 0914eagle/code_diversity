_earliest_train(N, M, trains):
    trains.sort(key=lambda x: x[1])  # Sort trains based on departure time
    earliest_start_time = float('inf')
    
    for train in trains:
        start_station, planned_departure, planned_arrival, delay = train
        current_time = start_time = planned_departure
        for next_train in trains:
            _, next_planned_departure, _, next_delay = next_train
            current_time = max(current_time, next_planned_departure - next_delay)
        if current_time - start_time >= 1800:
            earliest_start_time = min(earliest_start_time, start_time)
    
    return earliest_start_time if earliest_start_time != float('inf') else "impossible"

if __name__ == "__main__":
    N, M = map(int, input().split())
    trains = [list(map(int, input().split())) for _ in range(M)]
    
    result = find_earliest_train(N, M, trains)
    print(result)
