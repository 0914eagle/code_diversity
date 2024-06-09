
def get_min_time(n, m, railways):
    # Initialize a graph with the given railways
    graph = {i: set() for i in range(1, n + 1)}
    for u, v in railways:
        graph[u].add(v)
        graph[v].add(u)
    
    # Find all possible routes from town 1 to town n
    routes = []
    for route in dfs(graph, 1, n):
        routes.append(route)
    
    # Find the minimum time needed for the bus and the train to reach town n
    min_time = float('inf')
    for route in routes:
        time = 0
        for i in range(len(route) - 1):
            u, v = route[i], route[i + 1]
            time += 1
            if u != v and u in graph[v] and v in graph[u]:
                time += 1
        min_time = min(min_time, time)
    
    return min_time

def dfs(graph, start, end):
    if start == end:
        yield [start]
        return
    for neighbor in graph[start]:
        for path in dfs(graph, neighbor, end):
            yield [start] + path

if __name__ == '__main__':
    n, m = map(int, input().split())
    railways = []
    for _ in range(m):
        u, v = map(int, input().split())
        railways.append((u, v))
    print(get_min_time(n, m, railways))

