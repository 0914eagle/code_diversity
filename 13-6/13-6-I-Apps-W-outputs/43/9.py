
def count_ways(n):
    # Initialize a list to store the number of ways to fill the parking lot
    ways = [0] * (n + 1)

    # Base case: when n is 0, there is only one way to fill the parking lot (no cars)
    ways[0] = 1

    # Base case: when n is 1, there are 4 ways to fill the parking lot (4 different car makes)
    ways[1] = 4

    # Induction step: for each n >= 2, calculate the number of ways to fill the parking lot
    for i in range(2, n + 1):
        # There are 4 different car makes, so the total number of ways to fill the parking lot is the sum of the number of ways to fill the parking lot with each car make
        ways[i] = ways[i - 1] * 4

    return ways[n]

