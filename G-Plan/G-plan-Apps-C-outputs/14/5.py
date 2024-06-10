nstruct_dance_floor(N, K, sequence):
    graph = [0] * N
    for i in range(N):
        graph[i] = i + 1

    for i in range(N):
        if graph[i] == i + 1:
            current = i
            for _ in range(K):
                current = sequence[current] - 1
            graph[i] = current + 1

    return graph

if __name__ == "__main__":
    N, K = map(int, input().split())
    sequence = list(map(int, input().split()))

    result = reconstruct_dance_floor(N, K, sequence)
    if any(result[i] == i + 1 for i in range(N)):
        print("Impossible")
    else:
        print(*result)
