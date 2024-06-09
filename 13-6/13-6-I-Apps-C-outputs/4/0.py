
def get_min_hours(n, m, roads):
    # Initialize a graph with the given railways
    graph = [[] for _ in range(n + 1)]
    for u, v in roads:
        graph[u].append(v)
        graph[v].append(u)

    # Find the shortest path between the starting town (1) and the destination town (n) using Dijkstra's algorithm
    dist, prev = dijkstra(graph, 1, n)

    # If there is no path between the starting and destination towns, return -1
    if dist[n] == float('inf'):
        return -1

    # Initialize the minimum hours needed for the bus and train to reach town n
    min_hours_bus = 0
    min_hours_train = 0

    # Follow the shortest path from the starting town to the destination town to calculate the minimum hours needed for the bus and train to reach town n
    curr_town = n
    while curr_town != 1:
        prev_town = prev[curr_town]
        if prev_town in graph[curr_town]:
            min_hours_bus += 1
        else:
            min_hours_train += 1
        curr_town = prev_town

    return max(min_hours_bus, min_hours_train)

def dijkstra(graph, start, dest):
    # Initialize the distance and previous node arrays
    dist = [float('inf')] * (len(graph) + 1)
    prev = [None] * (len(graph) + 1)

    # Set the starting node's distance to 0 and its previous node to None
    dist[start] = 0
    prev[start] = None

    # Create a priority queue to store the nodes to visit
    pq = [(0, start)]

    # Loop until the priority queue is empty
    while pq:
        # Get the node with the smallest distance from the priority queue
        node = heappop(pq)[1]

        # If the node is the destination node, return the distance and previous node arrays
        if node == dest:
            return dist, prev

        # Loop through the node's neighbors
        for neighbor in graph[node]:
            # If the neighbor has not been visited, calculate its distance and previous node
            if dist[neighbor] == float('inf'):
                dist[neighbor] = dist[node] + 1
                prev[neighbor] = node

                # Add the neighbor to the priority queue
                heappush(pq, (dist[neighbor], neighbor))

    # If the destination node has not been found, return the distance and previous node arrays
    return dist, prev

if __name__ == '__main__':
    n, m = map(int, input().split())
    roads = []
    for _ in range(m):
        u, v = map(int, input().split())
        roads.append((u, v))
    print(get_min_hours(n, m, roads))

