
def read_input():
    N, M = map(int, input().split())
    edges = []
    for _ in range(M):
        a, b, c = map(int, input().split())
        edges.append((a, b, c))
    return N, M, edges

def find_path(N, edges):
    visited = [False] * (N + 1)
    queue = [(1, 0)]
    while queue:
        vertex, score = queue.pop(0)
        if vertex == N:
            return score
        for edge in edges:
            if edge[0] == vertex and not visited[edge[1]]:
                visited[edge[1]] = True
                queue.append((edge[1], score + edge[2]))
    return -1

def solve():
    N, M, edges = read_input()
    score = find_path(N, edges)
    if score == -1:
        print("inf")
    else:
        print(score)

if __name__ == '__main__':
    solve()

