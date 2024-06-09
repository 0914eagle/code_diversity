
def number_of_ways_to_fill_parking_lot(n):
    # Initialize a list to store the number of ways to fill the parking lot
    ways = [0] * (n + 1)
    ways[0] = 1
    
    # Loop through each car make
    for i in range(1, n + 1):
        # Loop through each combination of car makes
        for j in range(i):
            # Add the number of ways to fill the parking lot with the current combination of car makes
            ways[i] += ways[j]
    
    return ways[n]

