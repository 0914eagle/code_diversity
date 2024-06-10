
from collections import deque

def construct_graph(n, adjacency_matrix):
    graph = {}
    for i in range(n):
        graph[i + 1] = [j + 1 for j in range(n) if adjacency_matrix[i][j] == '1']
    return graph

def shortest_good_subsequence(n, adjacency_matrix, m, path):
    graph = construct_graph(n, adjacency_matrix)
    path_set = set(path)
    start_vertex = path[0]
    end_vertex = path[-1]
    
    queue = deque([(start_vertex, [start_vertex])])
    while queue:
        current_vertex, current_path = queue.popleft()
        if current_vertex == end_vertex and set(current_path) == path_set:
            return len(current_path), current_path
        
        for neighbor in graph[current_vertex]:
            if neighbor in path and neighbor not in current_path:
                queue.append((neighbor, current_path + [neighbor]))

if __name__ == "__main__":
    n = int(input())
    adjacency_matrix = [input().strip() for _ in range(n)]
    m = int(input())
    path = list(map(int, input().split()))
    
    length, subsequence = shortest_good_subsequence(n, adjacency_matrix, m, path)
    print(length)
    print(*subsequence)
