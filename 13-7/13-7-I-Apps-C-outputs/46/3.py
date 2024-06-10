
def get_cost_of_cheapest_network(buildings, connections, insecure_buildings, cost):
    # Initialize a graph with the given buildings as nodes
    graph = {building: set() for building in buildings}

    # Add edges to the graph based on the given connections
    for connection in connections:
        graph[connection[0]].add(connection[1])
        graph[connection[1]].add(connection[0])

    # Find the shortest path between all pairs of buildings using Dijkstra's algorithm
    distances = dijkstra(graph, insecure_buildings[0])

    # Calculate the total cost of the cheapest network
    total_cost = 0
    for building in buildings:
        total_cost += distances[building] * cost[building]

    return total_cost

def dijkstra(graph, start):
    # Initialize the distances from the start building to all other buildings as infinity
    distances = {building: float('inf') for building in graph}
    distances[start] = 0

    # Initialize a priority queue with the start building
    queue = [(0, start)]

    # Loop until the queue is empty
    while queue:
        # Get the building with the shortest distance from the queue
        distance, building = heapq.heappop(queue)

        # If the building has already been processed, skip it
        if distance > distances[building]:
            continue

        # Update the distances of the neighboring buildings
        for neighbor in graph[building]:
            new_distance = distance + 1
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(queue, (new_distance, neighbor))

    return distances

def main():
    # Read the input
    buildings, connections, insecure_buildings, cost = read_input()

    # Find the cheapest network
    cost_of_cheapest_network = get_cost_of_cheapest_network(buildings, connections, insecure_buildings, cost)

    # Print the result
    print(cost_of_cheapest_network)

def read_input():
    # Read the number of buildings, connections, and insecure buildings
    n, m, p = map(int, input().split())

    # Read the insecure buildings
    insecure_buildings = set(map(int, input().split()))

    # Read the connections
    connections = []
    for _ in range(m):
        x, y, cost = map(int, input().split())
        connections.append((x, y, cost))

    # Read the cost of each building
    cost = {building: 0 for building in range(1, n + 1)}
    for connection in connections:
        cost[connection[0]] += connection[2]
        cost[connection[1]] += connection[2]

    return range(1, n + 1), connections, insecure_buildings, cost

if __name__ == '__main__':
    main()

