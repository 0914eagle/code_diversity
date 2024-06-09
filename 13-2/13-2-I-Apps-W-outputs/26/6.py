
def count_distinct_ball_orders(n, throws):
    # Initialize the number of distinct ball orders to 1
    distinct_orders = 1

    # Iterate over each throw
    for i in range(n - 1):
        # Calculate the number of distinct ball orders after this throw
        distinct_orders *= throws[i] * (n - i)

        # Calculate the number of ball orders that will be repeated after this throw
        repeated_orders = throws[i] * (throws[i] - 1) // 2

        # Subtract the number of repeated ball orders from the total number of distinct ball orders
        distinct_orders -= repeated_orders

        # Modulo the result by 1000000007 to avoid overflow
        distinct_orders %= 1000000007

    return distinct_orders

