
def find_cheapest_network(n, m, p, insecure_buildings, cost_matrix):
    # Initialize a graph with n nodes and m edges
    graph = [[] for _ in range(n)]
    for i in range(m):
        x, y, cost = cost_matrix[i]
        graph[x - 1].append((y - 1, cost))
        graph[y - 1].append((x - 1, cost))
    
    # Find the shortest path between all pairs of nodes using Dijkstra's algorithm
    dist = [float('inf') for _ in range(n)]
    dist[0] = 0
    q = [(0, 0)]
    while q:
        node, dist_node = heappop(q)
        if dist_node > dist[node]:
            continue
        for neighbor, cost in graph[node]:
            new_dist = dist_node + cost
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heappush(q, (neighbor, new_dist))
    
    # Check if the security measure is satisfied
    for i in range(n):
        for j in range(i + 1, n):
            if dist[i] != float('inf') and dist[j] != float('inf') and dist[i] + dist[j] < dist[j]:
                return -1
    
    # Return the cheapest network cost
    return dist[n - 1]

def main():
    n, m, p = map(int, input().split())
    insecure_buildings = set(map(int, input().split()))
    cost_matrix = []
    for _ in range(m):
        x, y, cost = map(int, input().split())
        cost_matrix.append((x, y, cost))
    print(find_cheapest_network(n, m, p, insecure_buildings, cost_matrix))

if __name__ == '__main__':
    main()

