
from collections import deque

def construct_graph(n, adjacency_matrix):
    graph = {}
    for i in range(n):
        graph[i + 1] = [j + 1 for j in range(n) if adjacency_matrix[i][j] == '1']
    return graph

def find_shortest_good_subsequence(n, adjacency_matrix, m, path):
    graph = construct_graph(n, adjacency_matrix)
    path_set = set(path)
    visited = set()
    queue = deque([(path[0], [path[0]])])

    while queue:
        current_vertex, current_path = queue.popleft()
        visited.add(current_vertex)

        if len(current_path) >= 2 and set(current_path) == path_set:
            return len(current_path), current_path

        for neighbor in graph[current_vertex]:
            if neighbor not in visited:
                queue.append((neighbor, current_path + [neighbor]))

n = int(input())
adjacency_matrix = [input() for _ in range(n)]
m = int(input())
path = list(map(int, input().split()))

length, subsequence = find_shortest_good_subsequence(n, adjacency_matrix, m, path)
print(length)
print(*subsequence)
