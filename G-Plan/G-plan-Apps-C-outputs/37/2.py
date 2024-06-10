_earliest_train(N, M, trains):
    trains.sort(key=lambda x: x[1])  # Sort trains based on departure time
    earliest_time = float('inf')
    
    for train in trains:
        start_time = train[1]
        delay = 0
        
        for t in trains:
            if t[1] < start_time:
                delay += max(0, t[3] - (start_time - t[1]))
            else:
                delay += max(0, t[3])
        
        if delay >= 1800:
            earliest_time = min(earliest_time, start_time)
    
    return earliest_time if earliest_time != float('inf') else "impossible"

if __name__ == "__main__":
    N, M = map(int, input().split())
    trains = [list(map(int, input().split())) for _ in range(M)]
    
    result = find_earliest_train(N, M, trains)
    print(result)
