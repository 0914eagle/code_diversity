_earliest_train(N, M, trains):
    def calculate_delay(start_time):
        current_time = start_time
        for train in trains:
            X, S, T, L = train
            if current_time <= S:
                current_time = S
            elif current_time > T:
                return float('inf')
            current_time += L
        return current_time

    trains.sort(key=lambda x: x[1])  # Sort trains based on departure time
    for start_time in range(trains[0][1] - 1800, trains[0][1] + 1):
        if calculate_delay(start_time) >= 1800:
            return start_time
    return "impossible"

if __name__ == "__main__":
    N, M = map(int, input().split())
    trains = [list(map(int, input().split())) for _ in range(M)]
    result = find_earliest_train(N, M, trains)
    print(result)
""