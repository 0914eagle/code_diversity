
from collections import deque

def construct_graph(n, adjacency_matrix):
    graph = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if adjacency_matrix[i][j] == '1':
                graph[i].append(j)
    return graph

def find_shortest_good_subsequence(n, graph, m, path):
    shortest_subsequence = []
    shortest_length = float('inf')

    for i in range(m):
        visited = [False] * n
        queue = deque([(path[i], [path[i]])])

        while queue:
            current, sequence = queue.popleft()
            visited[current - 1] = True

            if len(sequence) >= 2 and sequence[0] == path[0] and sequence[-1] == path[-1]:
                if len(sequence) < shortest_length:
                    shortest_length = len(sequence)
                    shortest_subsequence = sequence

            for neighbor in graph[current - 1]:
                if not visited[neighbor]:
                    queue.append((neighbor + 1, sequence + [neighbor + 1]))

    return shortest_length, shortest_subsequence

if __name__ == "__main__":
    n = int(input())
    adjacency_matrix = [input() for _ in range(n)]
    graph = construct_graph(n, adjacency_matrix)
    m = int(input())
    path = list(map(int, input().split()))

    length, subsequence = find_shortest_good_subsequence(n, graph, m, path)
    print(length)
    print(*subsequence)
