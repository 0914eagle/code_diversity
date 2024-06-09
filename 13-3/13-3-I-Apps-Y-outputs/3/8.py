
def f1(n, m, k, x_y_w, a_b):
    # convert x_y_w and a_b to dictionaries for faster access
    x_y_w = {(x, y): w for x, y, w in x_y_w}
    a_b = {a: b for a, b in a_b}

    # create a graph with n nodes and m edges
    graph = [[] for _ in range(n)]
    for x, y, w in x_y_w.items():
        graph[x - 1].append((y - 1, w))
        graph[y - 1].append((x - 1, w))

    # find the shortest path between each pair of districts using Dijkstra's algorithm
    dist = [float('inf') for _ in range(n)]
    prev = [None for _ in range(n)]
    dist[0] = 0
    q = [(0, 0)]
    while q:
        node, dist_node = heappop(q)
        if dist_node > dist[node]:
            continue
        for neighbor, weight in graph[node]:
            dist_neighbor = dist_node + weight
            if dist_neighbor < dist[neighbor]:
                dist[neighbor] = dist_neighbor
                prev[neighbor] = node
                heappush(q, (neighbor, dist_neighbor))

    # calculate the minimum total courier routes cost
    total_cost = 0
    for a, b in a_b.items():
        total_cost += dist[a - 1] + dist[b - 1]

    return total_cost

def f2(...):
    ...

if __name__ == '__main__':
    n, m, k = map(int, input().split())
    x_y_w = [tuple(map(int, input().split())) for _ in range(m)]
    a_b = [tuple(map(int, input().split())) for _ in range(k)]
    print(f1(n, m, k, x_y_w, a_b))

