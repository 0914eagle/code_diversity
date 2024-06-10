
def get_longest_wait_time(orders, roads):
    # Initialize variables
    longest_wait_time = 0
    current_time = 0
    delivery_schedule = []

    # Sort orders by time of placement
    orders.sort(key=lambda x: x[0])

    # Loop through orders
    for order in orders:
        # Get order details
        order_time = order[0]
        order_location = order[1]
        delivery_time = order[2]

        # Check if order is ready for delivery
        if current_time >= order_time:
            # Add order to delivery schedule
            delivery_schedule.append((order_location, delivery_time))

            # Update longest wait time
            longest_wait_time = max(longest_wait_time, delivery_time - order_time)

        # Move current time forward
        current_time = max(current_time, delivery_time)

    # Return longest wait time
    return longest_wait_time

def main():
    # Read input
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

    # Find longest wait time
    longest_wait_time = get_longest_wait_time(orders, roads)

    # Print result
    print(longest_wait_time)

if __name__ == '__main__':
    main()

