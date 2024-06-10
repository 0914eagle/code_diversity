
def get_cheapest_network(n, m, p, insecure_buildings, costs):
    # Initialize a graph with n nodes and m edges
    graph = [[] for _ in range(n)]
    for i in range(m):
        x, y, cost = costs[i]
        graph[x - 1].append((y - 1, cost))
        graph[y - 1].append((x - 1, cost))
    
    # Dijkstra's algorithm to find the shortest path between all pairs of nodes
    dist = [float('inf')] * n
    dist[0] = 0
    q = [(0, 0)]
    while q:
        node, cost = heapq.heappop(q)
        if dist[node] < cost:
            continue
        for neighbor, neighbor_cost in graph[node]:
            new_cost = cost + neighbor_cost
            if new_cost < dist[neighbor]:
                dist[neighbor] = new_cost
                heapq.heappush(q, (neighbor, new_cost))
    
    # Check if the network is secure
    for i in range(n):
        for j in range(n):
            if i != j and dist[i] != float('inf') and dist[j] != float('inf') and dist[i] + dist[j] < dist[j]:
                return -1
    
    # Return the cheapest network cost
    return dist[n - 1]

def main():
    n, m, p = map(int, input().split())
    insecure_buildings = set(map(int, input().split()))
    costs = []
    for i in range(m):
        x, y, cost = map(int, input().split())
        costs.append((x, y, cost))
    print(get_cheapest_network(n, m, p, insecure_buildings, costs))

if __name__ == '__main__':
    main()

