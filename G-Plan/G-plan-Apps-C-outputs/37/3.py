ulate_delay(departure, arrival, delay):
    return max(0, arrival - departure - delay)

def find_earliest_start_time(N, M, trains):
    trains.sort(key=lambda x: x[1])  # Sort trains by departure time
    earliest_start_time = float('inf')
    
    for i in range(M):
        current_time = trains[i][1]
        current_delay = 0
        
        for j in range(i):
            if trains[j][2] <= current_time:
                current_delay = max(current_delay, calculate_delay(trains[j][1], trains[j][2], trains[j][3]))
        
        if current_time - current_delay >= 1800:
            earliest_start_time = min(earliest_start_time, trains[i][1] - current_delay)
    
    return earliest_start_time if earliest_start_time != float('inf') else "impossible"

if __name__ == "__main__":
    N, M = map(int, input().split())
    trains = [list(map(int, input().split())) for _ in range(M)]
    
    result = find_earliest_start_time(N, M, trains)
    print(result)
