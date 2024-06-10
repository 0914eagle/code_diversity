
def reconstruct_arrows(N, K, sequence):
    graph = [0] * N
    for i in range(N):
        graph[i] = sequence[i] - 1
    arrows = [-1] * N
    
    for i in range(N):
        if arrows[i] == -1:
            visited = [False] * N
            visited[i] = True
            current = i
            for _ in range(K):
                current = graph[current]
                if visited[current]:
                    return "Impossible"
                visited[current] = True
            arrows[i] = current + 1
    return arrows

if __name__ == "__main__":
    N, K = map(int, input().split())
    sequence = list(map(int, input().split()))
    
    result = reconstruct_arrows(N, K, sequence)
    if result == "Impossible":
        print("Impossible")
    else:
        print(*result)
