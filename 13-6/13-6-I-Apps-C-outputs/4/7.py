
def f1(n, m, railways):
    # convert the railways into a graph
    graph = [[] for _ in range(n + 1)]
    for u, v in railways:
        graph[u].append(v)
        graph[v].append(u)
    
    # find the shortest path between town 1 and town n
    visited = [False] * (n + 1)
    queue = [(1, 0)]
    while queue:
        town, time = queue.pop(0)
        if town == n:
            return time
        for neighbor in graph[town]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append((neighbor, time + 1))
    
    return -1

def f2(n, m, railways):
    # convert the railways into a graph
    graph = [[] for _ in range(n + 1)]
    for u, v in railways:
        graph[u].append(v)
        graph[v].append(u)
    
    # find the shortest path between town 1 and town n
    visited = [False] * (n + 1)
    queue = [(1, 0)]
    while queue:
        town, time = queue.pop(0)
        if town == n:
            return time
        for neighbor in graph[town]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append((neighbor, time + 1))
    
    return -1

if __name__ == '__main__':
    n, m = map(int, input().split())
    railways = []
    for _ in range(m):
        u, v = map(int, input().split())
        railways.append((u, v))
    print(f1(n, m, railways))
    print(f2(n, m, railways))

