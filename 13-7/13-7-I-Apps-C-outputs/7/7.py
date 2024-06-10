
def get_distance(start, end, graph):
    visited = set()
    queue = [(start, 0)]
    while queue:
        current, distance = queue.pop(0)
        if current not in visited:
            visited.add(current)
            if current == end:
                return distance
            for neighbor in graph[current]:
                queue.append((neighbor, distance + 1))
    return -1

def bfs(start, end, graph):
    visited = set()
    queue = [(start, 0)]
    while queue:
        current, distance = queue.pop(0)
        if current not in visited:
            visited.add(current)
            if current == end:
                return distance
            for neighbor in graph[current]:
                queue.append((neighbor, distance + 1))
    return -1

def solve(n, a, b, edges):
    graph = {}
    for edge in edges:
        graph[edge[0]] = [edge[1], edge[2]]
    
    distance_a = bfs(a, b, graph)
    distance_b = bfs(b, a, graph)
    
    if distance_a == -1 and distance_b == -1:
        return "indistinguishable"
    elif distance_a != -1 and distance_b != -1:
        return min(distance_a, distance_b)
    else:
        return distance_a if distance_a != -1 else distance_b

if __name__ == '__main__':
    n, a, b = map(int, input().split())
    edges = []
    for _ in range(n):
        edges.append(list(map(int, input().split())))
    print(solve(n, a, b, edges))

