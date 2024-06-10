
def get_graph(n, f, w):
    graph = {}
    for i in range(n):
        graph[i] = []
    for i in range(n):
        graph[i].append((f[i], w[i]))
    return graph

def get_paths(graph, k):
    paths = []
    for i in range(len(graph)):
        paths.append([])
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j][1] == k:
                paths[i].append(graph[i][j][0])
    return paths

def get_sum_min(graph, k):
    paths = get_paths(graph, k)
    result = []
    for i in range(len(paths)):
        sum_weight = 0
        min_weight = float('inf')
        for j in range(len(paths[i])):
            sum_weight += graph[i][paths[i][j]][1]
            min_weight = min(min_weight, graph[i][paths[i][j]][1])
        result.append((sum_weight, min_weight))
    return result

def main():
    n, k = map(int, input().split())
    f = list(map(int, input().split()))
    w = list(map(int, input().split()))
    graph = get_graph(n, f, w)
    result = get_sum_min(graph, k)
    for i in range(len(result)):
        print(result[i][0], result[i][1])

if __name__ == '__main__':
    main()

