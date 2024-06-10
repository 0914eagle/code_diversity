
def is_connected(n, m, k, capacities, connections):
    # Initialize a graph with the given number of nodes
    graph = [[] for _ in range(n)]

    # Add edges to the graph
    for connection in connections:
        graph[connection[0]].append(connection[1])
        graph[connection[1]].append(connection[0])

    # Initialize a variable to keep track of the number of edits made
    edits_made = 0

    # Loop through each node in the graph
    for node in range(n):
        # If the node has more than one connection, try to remove an edge
        if len(graph[node]) > 1:
            # Find the neighbor with the lowest capacity
            neighbor_with_lowest_capacity = None
            lowest_capacity = float('inf')
            for neighbor in graph[node]:
                if capacities[neighbor] < lowest_capacity:
                    neighbor_with_lowest_capacity = neighbor
                    lowest_capacity = capacities[neighbor]

            # If the lowest capacity neighbor has a capacity of 1, we cannot remove the edge
            if lowest_capacity == 1:
                return "no"

            # Remove the edge between the node and the neighbor with the lowest capacity
            graph[node].remove(neighbor_with_lowest_capacity)
            graph[neighbor_with_lowest_capacity].remove(node)
            edits_made += 1

            # If we have made the maximum number of edits allowed, return "no"
            if edits_made == k:
                return "no"

    # If we have reached this point, all nodes have at most one connection, so the graph is connected
    return "yes"

def main():
    n, m, k = map(int, input().split())
    capacities = list(map(int, input().split()))
    connections = []
    for _ in range(m):
        u, v = map(int, input().split())
        connections.append([u, v])
    print(is_connected(n, m, k, capacities, connections))

if __name__ == '__main__':
    main()

