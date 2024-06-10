
def get_longest_waiting_time(orders):
    # Sort the orders by their delivery time
    sorted_orders = sorted(orders, key=lambda x: x[2])

    # Initialize the longest waiting time to 0
    longest_waiting_time = 0

    # Iterate through the sorted orders
    for i in range(len(sorted_orders)):
        # Get the current order and its delivery time
        order = sorted_orders[i]
        delivery_time = order[2]

        # If the current order is not the first order, calculate the waiting time
        if i > 0:
            # Get the previous order and its delivery time
            previous_order = sorted_orders[i - 1]
            previous_delivery_time = previous_order[2]

            # Calculate the waiting time
            waiting_time = delivery_time - previous_delivery_time

            # Update the longest waiting time if necessary
            longest_waiting_time = max(longest_waiting_time, waiting_time)

    # Return the longest waiting time
    return longest_waiting_time

def get_optimal_delivery_schedule(orders, roads):
    # Initialize the delivery schedule as an empty list
    delivery_schedule = []

    # Sort the orders by their delivery time
    sorted_orders = sorted(orders, key=lambda x: x[2])

    # Iterate through the sorted orders
    for order in sorted_orders:
        # Get the order's delivery time and location
        delivery_time = order[2]
        location = order[1]

        # Find the shortest path from the pizzeria to the location
        shortest_path = find_shortest_path(roads, location)

        # Add the order to the delivery schedule
        delivery_schedule.append((delivery_time, location, shortest_path))

    # Return the optimal delivery schedule
    return delivery_schedule

def find_shortest_path(roads, location):
    # Initialize the shortest path as the road from the pizzeria to the location
    shortest_path = [location]

    # Iterate through the roads
    for road in roads:
        # If the road's start intersection is the location, add the road to the shortest path
        if road[0] == location:
            shortest_path.append(road[1])
            break

    # Return the shortest path
    return shortest_path

def main():
    # Read the input
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

    # Get the optimal delivery schedule
    delivery_schedule = get_optimal_delivery_schedule(orders, roads)

    # Get the longest waiting time
    longest_waiting_time = get_longest_waiting_time(delivery_schedule)

    # Print the result
    print(longest_waiting_time)

if __name__ == '__main__':
    main()

