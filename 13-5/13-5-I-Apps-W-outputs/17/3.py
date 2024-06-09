
def find_min_cost(n, m, k, roads, storages):
    # Initialize the graph with the given roads
    graph = [[] for _ in range(n + 1)]
    for u, v, l in roads:
        graph[u].append((v, l))
        graph[v].append((u, l))
    
    # Initialize the distances from each city to the bakery as infinity
    dist = [float('inf')] * (n + 1)
    dist[1] = 0
    
    # Initialize the priorities queue with the city 1 as the starting point
    pq = [(0, 1)]
    
    # Loop until the priority queue is empty
    while pq:
        # Get the current city and its distance from the bakery
        curr_dist, curr_city = heapq.heappop(pq)
        
        # If the current city is a storage, return the minimum distance
        if curr_city in storages:
            return curr_dist
        
        # Iterate over the neighbors of the current city
        for neighbor, length in graph[curr_city]:
            # If the distance from the bakery to the neighbor through the current city is shorter than the current distance, update the distance and add the neighbor to the priority queue
            new_dist = curr_dist + length
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))
    
    # If the bakery cannot be opened in any of the cities, return -1
    return -1

def main():
    n, m, k = map(int, input().split())
    roads = []
    for _ in range(m):
        u, v, l = map(int, input().split())
        roads.append((u, v, l))
    storages = list(map(int, input().split()))
    print(find_min_cost(n, m, k, roads, storages))

if __name__ == '__main__':
    main()

