
def calculate_completion_times(N, M, processing_times):
    completion_times = [0] * N
    for j in range(M):
        for i in range(N):
            if j == 0:
                completion_times[i] += processing_times[i][j]
            else:
                completion_times[i] = max(completion_times[i], completion_times[i - 1]) + processing_times[i][j]
    return completion_times

if __name__ == "__main__":
    N, M = map(int, input().split())
    processing_times = [list(map(int, input().split())) for _ in range(N)]
    completion_times = calculate_completion_times(N, M, processing_times)
    print(*completion_times)
