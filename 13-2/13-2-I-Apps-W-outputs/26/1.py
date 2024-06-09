
def count_distinct_ball_orders(n, throws):
    # Initialize a list to store the number of distinct ball orders
    distinct_orders = 1
    # Iterate over the throws
    for throw in throws:
        # Calculate the number of distinct ball orders after the current throw
        distinct_orders *= throw
        # Calculate the number of distinct ball orders after the current throw modulo 1000000007
        distinct_orders %= 1000000007
    # Return the number of distinct ball orders
    return distinct_orders

