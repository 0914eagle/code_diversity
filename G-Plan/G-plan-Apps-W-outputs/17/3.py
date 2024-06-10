
from collections import deque

def construct_graph(n, adjacency_matrix):
    graph = {}
    for i in range(n):
        graph[i + 1] = [j + 1 for j in range(n) if adjacency_matrix[i][j] == '1']
    return graph

def find_shortest_good_subsequence(n, adjacency_matrix, m, path):
    graph = construct_graph(n, adjacency_matrix)
    start_vertex = path[0]
    end_vertex = path[-1]

    def bfs(start):
        visited = set()
        queue = deque([(start, [start])])

        while queue:
            current_vertex, current_path = queue.popleft()
            visited.add(current_vertex)

            if current_vertex == end_vertex:
                return current_path

            for neighbor in graph[current_vertex]:
                if neighbor not in visited:
                    queue.append((neighbor, current_path + [neighbor]))

    shortest_good_subsequence = bfs(start_vertex)
    return shortest_good_subsequence

if __name__ == "__main__":
    n = int(input())
    adjacency_matrix = [input() for _ in range(n)]
    m = int(input())
    path = list(map(int, input().split()))

    shortest_good_subsequence = find_shortest_good_subsequence(n, adjacency_matrix, m, path)
    print(len(shortest_good_subsequence))
    print(" ".join(map(str, shortest_good_subsequence)))
