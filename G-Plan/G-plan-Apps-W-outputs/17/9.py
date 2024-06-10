
from collections import deque

def construct_graph(n, adjacency_matrix):
    graph = {}
    for i in range(n):
        graph[i + 1] = [j + 1 for j in range(n) if adjacency_matrix[i][j] == '1']
    return graph

def shortest_good_subsequence(n, adjacency_matrix, m, path):
    graph = construct_graph(n, adjacency_matrix)
    start_vertex = path[0]
    end_vertex = path[-1]
    
    def bfs(start, end):
        queue = deque([(start, [start])])
        while queue:
            current, path = queue.popleft()
            if current == end:
                return path
            for neighbor in graph[current]:
                if neighbor not in path:
                    queue.append((neighbor, path + [neighbor]))
    
    shortest_subsequence = bfs(start_vertex, end_vertex)
    
    return len(shortest_subsequence), shortest_subsequence

if __name__ == "__main__":
    n = int(input())
    adjacency_matrix = [input() for _ in range(n)]
    m = int(input())
    path = list(map(int, input().split()))
    
    length, subsequence = shortest_good_subsequence(n, adjacency_matrix, m, path)
    print(length)
    print(" ".join(map(str, subsequence)))
