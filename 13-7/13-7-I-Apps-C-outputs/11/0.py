
def get_longest_wait_time(orders, roads):
    # Initialize variables
    longest_wait_time = 0
    current_time = 0
    roads_dict = {}
    orders_dict = {}

    # Create a dictionary of roads and their travel times
    for road in roads:
        roads_dict[road[0]] = road[2]

    # Create a dictionary of orders and their times
    for order in orders:
        orders_dict[order[0]] = order[1]

    # Sort the orders by their times
    sorted_orders = sorted(orders, key=lambda x: x[1])

    # Iterate through the sorted orders
    for order in sorted_orders:
        # Get the current order and its time
        current_order = order[0]
        current_order_time = order[1]

        # Get the previous order and its time
        previous_order = sorted_orders[sorted_orders.index(order) - 1][0]
        previous_order_time = sorted_orders[sorted_orders.index(order) - 1][1]

        # Calculate the travel time for the previous order
        travel_time = roads_dict[previous_order] + roads_dict[current_order]

        # Calculate the current time
        current_time += travel_time

        # Check if the current order is the first order
        if previous_order == 1:
            # If it is, set the current time to the order time
            current_time = current_order_time

        # Check if the current order is later than the previous order
        if current_order_time > previous_order_time:
            # If it is, add the travel time to the current time
            current_time += travel_time

        # Update the longest wait time
        longest_wait_time = max(longest_wait_time, current_time - current_order_time)

    return longest_wait_time

def main():
    # Read the input
    n, m = map(int, input().split())
    roads = []
    for i in range(m):
        u, v, d = map(int, input().split())
        roads.append((u, v, d))
    k = int(input())
    orders = []
    for i in range(k):
        s, u, t = map(int, input().split())
        orders.append((s, u, t))

    # Call the function to get the longest wait time
    longest_wait_time = get_longest_wait_time(orders, roads)

    # Print the result
    print(longest_wait_time)

if __name__ == '__main__':
    main()

