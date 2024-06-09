
def min_seconds(n, a):
    # Initialize the number of seconds needed
    seconds = 0
    # Initialize the number of chocolates in each box
    chocolates = a
    # Loop until all boxes are divisible by k
    while not all(map(lambda x: x % k == 0, chocolates)) for k in range(2, 1000001):
        # Find the box with the most chocolates
        max_index = chocolates.index(max(chocolates))
        # Move the most chocolates to the next box
        chocolates[max_index] -= 1
        chocolates[(max_index + 1) % n] += 1
        # Increment the number of seconds
        seconds += 1
    # If all boxes are divisible by k, return the number of seconds
    if all(map(lambda x: x % k == 0, chocolates)):
        return seconds
    # Otherwise, return -1
    return -1

