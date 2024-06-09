
def get_score(graph, start, end):
    if start == end:
        return 0
    
    neighbors = graph[start]
    if end not in neighbors:
        return -1
    
    return neighbors[end] + get_score(graph, start, end - 1)

def solve(graph, start, end):
    if start == end:
        return 0
    
    max_score = -1
    for neighbor in graph[start]:
        score = get_score(graph, start, neighbor)
        if score != -1:
            max_score = max(max_score, score + solve(graph, neighbor, end))
    
    return max_score

def main():
    num_vertices, num_edges = map(int, input().split())
    graph = {i: {} for i in range(1, num_vertices + 1)}
    for _ in range(num_edges):
        a, b, c = map(int, input().split())
        graph[a][b] = c
    
    print(solve(graph, 1, num_vertices))

if __name__ == '__main__':
    main()

