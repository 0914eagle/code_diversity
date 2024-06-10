
def get_cheapest_network(n, m, p, insecure_buildings, costs):
    # Initialize a graph with n nodes and m edges
    graph = [[] for _ in range(n)]
    for i in range(m):
        x, y, cost = costs[i]
        graph[x - 1].append((y - 1, cost))
        graph[y - 1].append((x - 1, cost))
    
    # Initialize a set to store the insecure buildings
    insecure_set = set(insecure_buildings)
    
    # Initialize a priority queue to store the nodes to be visited
    pq = [(0, 0)]
    
    # Initialize a dictionary to store the minimum cost to reach each node
    dist = {0: 0}
    
    while pq:
        # Get the node with the minimum cost to visit
        node, cost = heapq.heappop(pq)
        
        # If the node is insecure, add its cost to the total cost
        if node in insecure_set:
            cost += dist[node]
        
        # If the node is the last node, return the total cost
        if node == n - 1:
            return cost
        
        # Iterate over the neighbors of the node
        for neighbor, neighbor_cost in graph[node]:
            # If the neighbor has not been visited yet, add it to the priority queue
            if neighbor not in dist:
                heapq.heappush(pq, (neighbor, cost + neighbor_cost))
                dist[neighbor] = cost + neighbor_cost
    
    # If the network is not possible, return "impossible"
    return "impossible"

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

