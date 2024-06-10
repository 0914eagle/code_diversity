
from collections import deque

def construct_graph(n, adjacency_matrix):
    graph = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if adjacency_matrix[i][j] == '1':
                graph[i].append(j)
    return graph

def shortest_good_subsequence(n, adjacency_matrix, m, path):
    graph = construct_graph(n, adjacency_matrix)
    start_vertex = path[0]
    end_vertex = path[-1]

    visited = set()
    queue = deque([(start_vertex, [start_vertex])])

    while queue:
        current_vertex, current_path = queue.popleft()
        visited.add(current_vertex)

        if current_vertex == end_vertex:
            return len(current_path), current_path

        for neighbor in graph[current_vertex]:
            if neighbor not in visited:
                new_path = current_path + [neighbor]
                queue.append((neighbor, new_path))

if __name__ == "__main__":
    n = int(input())
    adjacency_matrix = [input() for _ in range(n)]
    m = int(input())
    path = list(map(int, input().split()))

    k, v = shortest_good_subsequence(n, adjacency_matrix, m, path)
    print(k)
    print(*v)
