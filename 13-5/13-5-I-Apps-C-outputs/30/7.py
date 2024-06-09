
def get_longest_wait_time(orders, roads):
    # Initialize variables
    longest_wait_time = 0
    current_time = 0
    delivery_schedule = []

    # Sort the orders by time of placement
    orders.sort(key=lambda x: x[0])

    # Loop through the orders
    for order in orders:
        # Get the time of placement and destination
        time_of_placement = order[0]
        destination = order[1]

        # Find the shortest path from the pizzeria to the destination
        path = find_shortest_path(roads, current_time, destination)

        # Add the path to the delivery schedule
        delivery_schedule.append(path)

        # Update the current time
        current_time += path[-1][1]

        # Calculate the wait time
        wait_time = current_time - time_of_placement

        # Update the longest wait time
        longest_wait_time = max(longest_wait_time, wait_time)

    return longest_wait_time

def find_shortest_path(roads, current_time, destination):
    # Initialize variables
    visited = set()
    queue = [(current_time, 0, [])]

    # Loop through the queue
    while queue:
        # Get the current node and its attributes
        time, distance, path = queue.pop(0)
        node = path[-1]

        # If the node is the destination, return the path
        if node == destination:
            return path

        # If the node has not been visited, mark it as visited and add its neighbors to the queue
        if node not in visited:
            visited.add(node)
            for neighbor in roads[node]:
                queue.append((time + neighbor[1], distance + neighbor[0], path + [neighbor[2]]))

    # If no path is found, return an empty list
    return []

def main():
    # Read the input
    n, m = map(int, input().split())
    roads = {}
    for _ in range(m):
        u, v, d = map(int, input().split())
        if u not in roads:
            roads[u] = []
        if v not in roads:
            roads[v] = []
        roads[u].append((d, v, u))
        roads[v].append((d, u, v))
    k = int(input())
    orders = []
    for _ in range(k):
        s, u, t = map(int, input().split())
        orders.append((s, u, t))

    # Find the longest wait time
    longest_wait_time = get_longest_wait_time(orders, roads)

    # Print the result
    print(longest_wait_time)

if __name__ == '__main__':
    main()

