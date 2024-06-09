
def f1(N, M, edges):
    # Initialize the graph with N vertices and M edges
    graph = [[] for _ in range(N)]
    for i in range(M):
        graph[edges[i][0] - 1].append((edges[i][1], edges[i][2]))
    
    # Initialize the score and the current vertex
    score = 0
    current_vertex = 0
    
    # Loop through the edges and update the score and the current vertex
    for i in range(M):
        for j in range(len(graph[current_vertex])):
            if graph[current_vertex][j][0] == edges[i][1]:
                score += graph[current_vertex][j][1]
                current_vertex = edges[i][1] - 1
                break
    
    return score

def f2(N, M, edges):
    # Initialize the graph with N vertices and M edges
    graph = [[] for _ in range(N)]
    for i in range(M):
        graph[edges[i][0] - 1].append((edges[i][1], edges[i][2]))
    
    # Initialize the score and the current vertex
    score = 0
    current_vertex = 0
    
    # Loop through the edges and update the score and the current vertex
    for i in range(M):
        for j in range(len(graph[current_vertex])):
            if graph[current_vertex][j][0] == edges[i][1]:
                score += graph[current_vertex][j][1]
                current_vertex = edges[i][1] - 1
                break
    
    return score

if __name__ == '__main__':
    N, M = map(int, input().split())
    edges = []
    for i in range(M):
        a, b, c = map(int, input().split())
        edges.append((a, b, c))
    print(f1(N, M, edges))

