
def find_min_cost(n, m, k, roads, storages):
    # Initialize graph with distances between cities
    graph = {i: {} for i in range(1, n + 1)}
    for u, v, l in roads:
        graph[u][v] = l
        graph[v][u] = l

    # Initialize distances from each city to the bakery as infinity
    dist = {i: float('inf') for i in range(1, n + 1)}
    dist[1] = 0

    # Initialize priorities queue with city 1 as the starting point
    pq = [(0, 1)]

    while pq:
        # Get the city with the shortest distance from the priority queue
        dist_city, city = heapq.heappop(pq)

        # If the city is a storage, return the distance
        if city in storages:
            return dist_city

        # If the city has already been processed, skip it
        if dist_city > dist[city]:
            continue

        # Iterate over the city's neighbors
        for neighbor, weight in graph[city].items():
            # Calculate the new distance to the neighbor
            new_dist = dist_city + weight

            # If the new distance is less than the current distance, update the distance and add the neighbor to the priority queue
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))

    # If no storage is found, return -1
    return -1

def main():
    n, m, k = map(int, input().split())
    roads = []
    for _ in range(m):
        u, v, l = map(int, input().split())
        roads.append((u, v, l))
    storages = set(map(int, input().split()))
    print(find_min_cost(n, m, k, roads, storages))

if __name__ == '__main__':
    main()

