
def reconstruct_arrows(N, K, sequence):
    graph = {i: 0 for i in range(1, N + 1)}
    for i in range(N):
        graph[i + 1] = sequence[i]

    arrows = [0] * N

    for i in range(N):
        if arrows[i] == 0:
            visited = set()
            visited.add(i + 1)
            current = i + 1
            for _ in range(K):
                current = graph[current]
                if current in visited or current == i + 1:
                    return "Impossible"
                visited.add(current)
            arrows[i] = current

    return arrows


if __name__ == "__main__":
    N, K = map(int, input().split())
    sequence = list(map(int, input().split()))
    
    result = reconstruct_arrows(N, K, sequence)
    if result == "Impossible":
        print("Impossible")
    else:
        print(*result)
