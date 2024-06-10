
def reconstruct_dance_floor(N, K, sequence):
    graph = [0] * N
    for i in range(N):
        graph[i] = i + 1

    for i in range(N):
        if graph[i] == sequence[i]:
            return "Impossible"

    for i in range(N):
        if graph[sequence[i] - 1] != 0:
            return "Impossible"
        graph[sequence[i] - 1] = i + 1

    return graph

if __name__ == "__main__":
    N, K = map(int, input().split())
    sequence = list(map(int, input().split()))

    result = reconstruct_dance_floor(N, K, sequence)
    if result == "Impossible":
        print("Impossible")
    else:
        print(*result)
