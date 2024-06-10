
def get_input():
    n, m = map(int, input().split())
    roads = []
    for _ in range(m):
        a, b, d = map(int, input().split())
        roads.append((a, b, d))
    return n, m, roads

def build_graph(roads):
    graph = {}
    for a, b, d in roads:
        if a not in graph:
            graph[a] = {}
        graph[a][b] = d
    return graph

def find_shortest_path(graph, start, end):
    visited = set()
    queue = [(0, start)]
    while queue:
        dist, node = heapq.heappop(queue)
        if node == end:
            return dist
        if node in visited:
            continue
        visited.add(node)
        for neighbor, weight in graph[node].items():
            heapq.heappush(queue, (dist + weight, neighbor))
    return float('inf')

def find_route(graph, start, end):
    visited = set()
    queue = [(0, start)]
    while queue:
        dist, node = heapq.heappop(queue)
        if node == end:
            return dist
        if node in visited:
            continue
        visited.add(node)
        for neighbor, weight in graph[node].items():
            heapq.heappush(queue, (dist + weight, neighbor))
    return float('inf')

def solve(n, m, roads):
    graph = build_graph(roads)
    dist = find_route(graph, 0, 1)
    if dist == float('inf'):
        return "impossible"
    path = []
    node = 1
    while node != 0:
        path.append(node)
        node = graph[node][0]
    path.reverse()
    return " ".join(str(i) for i in path)

def main():
    n, m, roads = get_input()
    print(solve(n, m, roads))

if __name__ == '__main__':
    main()

