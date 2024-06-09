
def f1(N, M, edges):
    # Initialize the graph with N vertices and M edges
    graph = [[] for _ in range(N)]
    for edge in edges:
        graph[edge[0] - 1].append((edge[1], edge[2]))

    # Initialize the maximum score to 0
    max_score = 0

    # Recursive function to find the maximum score
    def find_max_score(vertex, score):
        nonlocal max_score
        if vertex == N - 1:
            max_score = max(max_score, score)
            return
        for neighbor, weight in graph[vertex]:
            find_max_score(neighbor, score + weight)

    # Start the recursive function at vertex 0 with a score of 0
    find_max_score(0, 0)

    return max_score

def f2(N, M, edges):
    # Initialize the graph with N vertices and M edges
    graph = [[] for _ in range(N)]
    for edge in edges:
        graph[edge[0] - 1].append((edge[1], edge[2]))

    # Initialize the maximum score to 0
    max_score = 0

    # Iterative function to find the maximum score
    queue = [(0, 0)]
    while queue:
        vertex, score = queue.pop(0)
        if vertex == N - 1:
            max_score = max(max_score, score)
            continue
        for neighbor, weight in graph[vertex]:
            queue.append((neighbor, score + weight))

    return max_score

if __name__ == '__main__':
    N, M = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(M)]
    print(f1(N, M, edges))
    print(f2(N, M, edges))

