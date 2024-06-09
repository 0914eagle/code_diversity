
def get_score(graph, start, end):
    if start == end:
        return 0
    
    neighbors = graph[start]
    if end not in neighbors:
        return -1
    
    return neighbors[end] + get_score(graph, start, end - 1)

def main():
    num_vertices, num_edges = map(int, input().split())
    graph = {}
    
    for _ in range(num_edges):
        a, b, c = map(int, input().split())
        if a not in graph:
            graph[a] = {}
        graph[a][b] = c
    
    print(get_score(graph, 1, num_vertices))

if __name__ == '__main__':
    main()

