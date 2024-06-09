
def count_ways(n):
    # Initialize a list to store the number of ways to fill the parking lot
    ways = [0] * (n + 1)
    ways[0] = 1

    # Loop through each make of car
    for make in range(1, 5):
        # Loop through each number of cars of the current make
        for num_cars in range(1, n + 1):
            # Calculate the number of ways to fill the parking lot with the current make and number of cars
            ways[num_cars] += ways[num_cars - 1]

    # Return the number of ways to fill the parking lot
    return ways[n]

