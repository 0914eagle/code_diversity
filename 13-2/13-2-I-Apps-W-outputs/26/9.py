
def count_distinct_ball_orders(n, throws):
    # Initialize the number of distinct ball orders to 1
    num_distinct_orders = 1

    # Iterate over each throw
    for i in range(n - 1):
        # Calculate the number of distinct ball orders after this throw
        num_distinct_orders *= throws[i] * (n - i)

        # Calculate the number of duplicate ball orders after this throw
        num_duplicate_orders = throws[i] * (throws[i] - 1) // 2

        # Subtract the number of duplicate ball orders from the total number of distinct ball orders
        num_distinct_orders -= num_duplicate_orders

        # Modulo the result to avoid overflow
        num_distinct_orders %= 1000000007

    return num_distinct_orders

