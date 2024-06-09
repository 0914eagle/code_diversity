
def f1(n, m, q):
    # Initialize a graph with n nodes and m edges
    graph = [[] for _ in range(n)]
    for _ in range(m):
        a, b, w = map(int, input().split())
        graph[a-1].append((b-1, w))
        graph[b-1].append((a-1, w))
    
    # Find the shortest path between each pair of nodes
    distances = [[float('inf') for _ in range(n)] for _ in range(n)]
    for i in range(n):
        distances[i][i] = 0
    for k in range(n):
        for i in range(n):
            for j in range(n):
                distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])
    
    # Return the cost of sending a crystal from s to t on day q
    s, t = map(int, input().split())
    return distances[s-1][t-1]

def f2(n, m, q):
    # Initialize a graph with n nodes and m edges
    graph = [[] for _ in range(n)]
    for _ in range(m):
        a, b, w = map(int, input().split())
        graph[a-1].append((b-1, w))
        graph[b-1].append((a-1, w))
    
    # Find the shortest path between each pair of nodes
    distances = [[float('inf') for _ in range(n)] for _ in range(n)]
    for i in range(n):
        distances[i][i] = 0
    for k in range(n):
        for i in range(n):
            for j in range(n):
                distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])
    
    # Return the cost of sending a crystal from s to t on day q
    s, t = map(int, input().split())
    return distances[s-1][t-1]

if __name__ == '__main__':
    n, m = map(int, input().split())
    q = int(input())
    for _ in range(q):
        s, t = map(int, input().split())
        print(f1(n, m, q))
        print(f2(n, m, q))

