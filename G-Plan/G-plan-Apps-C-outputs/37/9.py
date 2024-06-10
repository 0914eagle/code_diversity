ulate_delay(planned_departure, planned_arrival, delay):
    return max(0, planned_arrival - planned_departure - delay)

def find_earliest_start_time(N, M, trains):
    trains.sort(key=lambda x: x[1])  # Sort trains by planned departure time
    earliest_start_time = float('inf')
    
    for i in range(M):
        current_start_time = trains[i][1]
        current_arrival_time = trains[i][2]
        current_delay = trains[i][3]
        
        if calculate_delay(current_start_time, current_arrival_time, current_delay) >= 1800:
            earliest_start_time = min(earliest_start_time, current_start_time)
    
    return earliest_start_time if earliest_start_time != float('inf') else "impossible"

if __name__ == "__main__":
    N, M = map(int, input().split())
    trains = [list(map(int, input().split())) for _ in range(M)]
    
    result = find_earliest_start_time(N, M, trains)
    print(result)
""