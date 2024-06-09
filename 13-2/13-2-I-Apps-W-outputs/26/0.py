
def count_distinct_ball_orders(n, throws):
    # Initialize a list to store the number of ways for each ball
    num_ways = [1] * n

    # Iterate over the throws
    for i in range(n - 1):
        # Swap the balls for each throw
        num_ways[i], num_ways[i + 1] = num_ways[i + 1], num_ways[i]

    # Return the number of distinct ways modulo 1000000007
    return sum(num_ways) % 1000000007

