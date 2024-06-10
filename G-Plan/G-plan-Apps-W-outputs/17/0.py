
from collections import deque

def construct_graph(n, adjacency_matrix):
    graph = {}
    for i in range(n):
        neighbors = []
        for j in range(n):
            if adjacency_matrix[i][j] == '1':
                neighbors.append(j)
        graph[i] = neighbors
    return graph

def shortest_good_subsequence(n, adjacency_matrix, m, path):
    graph = construct_graph(n, adjacency_matrix)
    start_vertex = path[0]
    end_vertex = path[-1]
    
    def bfs(start, end):
        queue = deque([(start, [start])])
        while queue:
            current, path_so_far = queue.popleft()
            if current == end:
                return path_so_far
            for neighbor in graph[current]:
                if neighbor not in path_so_far:
                    queue.append((neighbor, path_so_far + [neighbor]))
    
    shortest_path = bfs(start_vertex, end_vertex)
    return len(shortest_path), shortest_path

if __name__ == "__main__":
    n = int(input())
    adjacency_matrix = [input().strip() for _ in range(n)]
    m = int(input())
    path = list(map(int, input().split()))
    
    length, subsequence = shortest_good_subsequence(n, adjacency_matrix, m, path)
    print(length)
    print(" ".join(map(str, subsequence)))
