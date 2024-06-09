
def number_of_ways_to_fill_parking_lot(n):
    # Initialize a list to store the number of ways to fill the parking lot
    ways = [0] * (n + 1)
    ways[0] = 1

    # Loop through each car make
    for i in range(1, n + 1):
        # Loop through each possible number of cars of the current make
        for j in range(i, n + 1):
            # Add the number of ways to fill the parking lot with the current make and the previous makes
            ways[j] += ways[j - i]

    return ways[n]

