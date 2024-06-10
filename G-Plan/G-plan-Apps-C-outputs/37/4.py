_earliest_train(N, M, trains):
    trains.sort(key=lambda x: x[1])  # Sort trains based on departure time
    earliest_start_time = float('inf')
    
    for i in range(M):
        start_time = trains[i][1]
        delay = 0
        
        for j in range(i):
            if trains[j][3] > start_time:
                delay = max(delay, trains[j][3] - start_time)
        
        if delay >= 1800:
            earliest_start_time = min(earliest_start_time, start_time)
    
    return earliest_start_time if earliest_start_time != float('inf') else "impossible"

if __name__ == "__main__":
    N, M = map(int, input().split())
    trains = [list(map(int, input().split())) for _ in range(M)]
    
    result = find_earliest_train(N, M, trains)
    print(result)
