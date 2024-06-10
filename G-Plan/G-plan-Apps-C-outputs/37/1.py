_earliest_start_time(N, M, trains):
    trains.sort(key=lambda x: x[1])  # Sort trains by departure time
    earliest_start_time = float('inf')
    
    for train in trains:
        start_station, planned_departure, planned_arrival, delay = train
        current_time = start_time = planned_departure - delay
        
        for next_train in trains:
            next_start_station, next_planned_departure, next_planned_arrival, next_delay = next_train
            if next_start_station > start_station:
                current_time = max(current_time, next_planned_departure - delay)
        
        if current_time + (planned_arrival - planned_departure) >= 1800:
            earliest_start_time = min(earliest_start_time, start_time)
    
    return earliest_start_time if earliest_start_time != float('inf') else "impossible"

if __name__ == "__main__":
    N, M = map(int, input().split())
    trains = [list(map(int, input().split())) for _ in range(M)]
    
    result = find_earliest_start_time(N, M, trains)
    print(result)
