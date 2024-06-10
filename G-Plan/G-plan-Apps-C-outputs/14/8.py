
def reconstruct_arrows(N, K, sequence):
    graph = [0] * N
    for i in range(N):
        graph[i] = sequence[i] - 1

    arrows = [0] * N
    for i in range(N):
        arrows[i] = i + 1

    for _ in range(K):
        new_arrows = [0] * N
        for i in range(N):
            new_arrows[i] = arrows[graph[i]]
        arrows = new_arrows

    return arrows

if __name__ == "__main__":
    N, K = map(int, input().split())
    sequence = list(map(int, input().split()))

    result = reconstruct_arrows(N, K, sequence)
    print(*result)
