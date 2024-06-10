
def calculate_completion_times(N, M, processing_times):
    completion_times = []
    for i in range(N):
        time_taken = 0
        for j in range(M):
            time_taken += processing_times[i][j]
        completion_times.append(time_taken)
    return completion_times

if __name__ == "__main__":
    N, M = map(int, input().split())
    processing_times = [list(map(int, input().split())) for _ in range(N)]
    
    completion_times = calculate_completion_times(N, M, processing_times)
    print(*completion_times)
