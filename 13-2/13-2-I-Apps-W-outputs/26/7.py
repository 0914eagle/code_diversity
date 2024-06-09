
def count_distinct_ball_orders(n, throws):
    # Initialize a list to store the number of ways for each ball
    ways = [1] * n

    # Iterate over the throws
    for i in range(n - 1):
        # Swap the balls for the current throw
        ways[i], ways[i + 1] = ways[i + 1], ways[i]

    # Return the number of distinct ways modulo 1000000007
    return sum(ways) % 1000000007

