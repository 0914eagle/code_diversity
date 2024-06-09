
def get_cheapest_network(n, m, p, insecure_buildings, connections):
    # Initialize a graph with n nodes and 0 edges
    graph = [[] for _ in range(n)]

    # Add edges to the graph based on the connections
    for connection in connections:
        x, y, cost = connection
        graph[x - 1].append((y - 1, cost))
        graph[y - 1].append((x - 1, cost))

    # Find the minimum spanning tree of the graph
    mst = prim(graph, 0)

    # Initialize the total cost of the network to 0
    total_cost = 0

    # Iterate through the edges of the MST
    for edge in mst:
        # If the edge connects two insecure buildings, skip it
        if edge[0] in insecure_buildings and edge[1] in insecure_buildings:
            continue
        # Otherwise, add the cost of the edge to the total cost
        total_cost += edge[2]

    return total_cost

def prim(graph, start):
    # Initialize a priority queue with all nodes in the graph
    queue = [(0, start)]

    # Initialize a dictionary to keep track of the predecessor of each node
    predecessors = {node: None for node in range(len(graph))}

    # Initialize a set to keep track of the nodes that have been visited
    visited = set()

    # Loop until the queue is empty
    while queue:
        # Get the node with the minimum distance from the priority queue
        distance, node = heapq.heappop(queue)

        # If the node has already been visited, skip it
        if node in visited:
            continue

        # Mark the node as visited
        visited.add(node)

        # Iterate through the neighbors of the node
        for neighbor, weight in graph[node]:
            # If the neighbor has not been visited, add it to the priority queue
            if neighbor not in visited:
                heapq.heappush(queue, (distance + weight, neighbor))

            # Update the predecessor of the neighbor
            predecessors[neighbor] = node

    # Return the minimum spanning tree of the graph
    return [(predecessors[node], node, weight) for node, weight in graph[start]]

def main():
    n, m, p = map(int, input().split())
    insecure_buildings = set(map(int, input().split()))
    connections = []
    for _ in range(m):
        x, y, cost = map(int, input().split())
        connections.append((x, y, cost))
    print(get_cheapest_network(n, m, p, insecure_buildings, connections))

if __name__ == '__main__':
    main()

