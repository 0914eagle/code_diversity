
def get_path_weights(graph, k):
    n = len(graph)
    path_weights = [[0, 0] for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            if graph[i][j] != 0:
                path_weights[i][0] += graph[i][j]
                path_weights[i][1] = min(path_weights[i][1], graph[i][j])
    return path_weights

def get_vertex_weights(graph, k):
    n = len(graph)
    vertex_weights = [[0, 0] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] != 0:
                vertex_weights[i][0] += graph[i][j]
                vertex_weights[i][1] = min(vertex_weights[i][1], graph[i][j])
    return vertex_weights

def main():
    n, k = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]
    path_weights = get_path_weights(graph, k)
    vertex_weights = get_vertex_weights(graph, k)
    for i in range(n):
        print(path_weights[i][0], path_weights[i][1])
        print(vertex_weights[i][0], vertex_weights[i][1])

if __name__ == '__main__':
    main()

