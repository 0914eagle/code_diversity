
def solve(n, m, roads, orders):
    # Initialize a graph with n nodes and 0 edges
    graph = [[] for _ in range(n)]

    # Add edges to the graph
    for road in roads:
        u, v, d = road
        graph[u - 1].append((v - 1, d))
        graph[v - 1].append((u - 1, d))

    # Sort the orders by their time of arrival
    orders.sort(key=lambda x: x[0])

    # Initialize the delivery time for each order to 0
    delivery_times = [0] * len(orders)

    # Loop through the orders and calculate the delivery time for each order
    for i in range(len(orders)):
        order = orders[i]
        time = order[0]
        source = order[1] - 1
        destination = order[2] - 1

        # If this is the first order, set the delivery time to 0
        if i == 0:
            delivery_times[i] = 0
        else:
            # Find the previous order that was delivered from the same source
            previous_order = orders[i - 1]
            previous_source = previous_order[1] - 1
            previous_destination = previous_order[2] - 1

            # If the previous order was delivered from the same source,
            # calculate the delivery time based on the previous order's delivery time
            if previous_source == source:
                delivery_times[i] = delivery_times[i - 1] + graph[previous_destination][previous_source][1]
            # Otherwise, calculate the delivery time based on the shortest path from the source to the destination
            else:
                delivery_times[i] = delivery_times[i - 1] + shortest_path(graph, source, destination)

    # Return the maximum delivery time
    return max(delivery_times)

def shortest_path(graph, source, destination):
    # Initialize the distance from the source to infinity
    distance = [float('inf')] * len(graph)
    distance[source] = 0

    # Loop through the nodes in the graph
    for i in range(len(graph)):
        # If we have reached the destination, return the distance
        if i == destination:
            return distance[i]
        # Otherwise, loop through the neighbors of the current node
        for neighbor, weight in graph[i]:
            # If the distance to the neighbor is greater than the current distance plus the weight,
            # update the distance to the neighbor
            if distance[i] + weight < distance[neighbor]:
                distance[neighbor] = distance[i] + weight

    # If the destination is not reachable, return infinity
    return float('inf')

def main():
    n, m = map(int, input().split())
    roads = []
    for _ in range(m):
        u, v, d = map(int, input().split())
        roads.append((u, v, d))
    k = int(input())
    orders = []
    for _ in range(k):
        s, u, t = map(int, input().split())
        orders.append((s, u, t))
    print(solve(n, m, roads, orders))

if __name__ == '__main__':
    main()

