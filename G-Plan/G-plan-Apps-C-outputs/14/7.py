
def reconstruct_arrows(N, K, sequence):
    arrows = [-1] * N
    for i in range(N):
        arrows[i] = sequence[i] - 1
    return arrows

def is_valid_placement(arrows):
    visited = [False] * len(arrows)
    for i in range(len(arrows)):
        if visited[i]:
            continue
        visited[i] = True
        next_arrow = arrows[i]
        while next_arrow != i:
            if visited[next_arrow]:
                return False
            visited[next_arrow] = True
            next_arrow = arrows[next_arrow]
    return True

def find_arrows(N, K, sequence):
    arrows = reconstruct_arrows(N, K, sequence)
    if is_valid_placement(arrows):
        return arrows
    return "Impossible"

if __name__ == "__main__":
    N, K = map(int, input().split())
    sequence = list(map(int, input().split()))
    result = find_arrows(N, K, sequence)
    if result == "Impossible":
        print(result)
    else:
        print(*result)
