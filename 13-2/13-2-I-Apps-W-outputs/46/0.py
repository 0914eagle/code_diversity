
def get_maximal_orders(orders):
    # Sort the orders by their start time
    sorted_orders = sorted(orders, key=lambda x: x[0])

    # Initialize the maximum number of accepted orders to 0
    max_accepted_orders = 0

    # Initialize the current time to 0
    current_time = 0

    # Iterate through the sorted orders
    for order in sorted_orders:
        # If the start time of the current order is greater than the current time, we can accept the order
        if order[0] > current_time:
            # Update the current time to the finish time of the current order
            current_time = order[1]
            # Increment the maximum number of accepted orders
            max_accepted_orders += 1

    return max_accepted_orders

