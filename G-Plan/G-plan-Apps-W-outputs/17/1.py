truct_graph(n, adjacency_matrix):
    graph = {}
    for i in range(n):
        neighbors = []
        for j in range(n):
            if adjacency_matrix[i][j] == '1':
                neighbors.append(j + 1)
        graph[i + 1] = neighbors
    return graph

def shortest_good_subsequence(n, adjacency_matrix, m, path):
    graph = construct_graph(n, adjacency_matrix)
    start_vertex = path[0]
    end_vertex = path[-1]
    
    queue = [(start_vertex, [start_vertex])]
    while queue:
        current_vertex, current_path = queue.pop(0)
        if current_vertex == end_vertex:
            return len(current_path), current_path
        
        for neighbor in graph[current_vertex]:
            if neighbor in path[path.index(current_vertex) + 1:]:
                new_path = current_path + [neighbor]
                queue.append((neighbor, new_path))

if __name__ == "__main__":
    n = int(input())
    adjacency_matrix = [input() for _ in range(n)]
    m = int(input())
    path = list(map(int, input().split()))
    
    length, subsequence = shortest_good_subsequence(n, adjacency_matrix, m, path)
    print(length)
    print(" ".join(map(str, subsequence))