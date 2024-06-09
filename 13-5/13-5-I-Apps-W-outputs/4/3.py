
def get_score(graph, start, end):
    
    if start == end:
        return 0
    
    neighbors = graph[start]
    if end in neighbors:
        return neighbors[end]
    
    max_score = -float('inf')
    for neighbor, weight in neighbors.items():
        max_score = max(max_score, weight + get_score(graph, neighbor, end))
    
    return max_score

def main():
    num_vertices, num_edges = map(int, input().split())
    graph = {i: {} for i in range(1, num_vertices + 1)}
    
    for _ in range(num_edges):
        a, b, c = map(int, input().split())
        graph[a][b] = c
    
    print(get_score(graph, 1, num_vertices))

if __name__ == '__main__':
    main()

