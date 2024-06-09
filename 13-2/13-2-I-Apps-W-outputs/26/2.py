
def count_distinct_ball_orders(n, throws):
    # Initialize the number of distinct ball orders to 1
    distinct_orders = 1

    # Iterate over each throw
    for i in range(n - 1):
        # Calculate the number of distinct ball orders after this throw
        distinct_orders *= throws[i] * (n - i)

        # Reduce the number of distinct ball orders modulo 1000000007
        distinct_orders %= 1000000007

    return distinct_orders

