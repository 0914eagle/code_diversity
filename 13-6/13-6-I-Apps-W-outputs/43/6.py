
def solve(n):
    # Initialize a list to store the number of ways to fill the parking lot
    ways = 0

    # Loop through the four car makes
    for make in ["A", "B", "M", "Z"]:
        # Calculate the number of cars of this make that can be placed in the parking lot
        num_cars = n // 2

        # Calculate the number of ways to place the cars of this make in the parking lot
        ways += num_cars * (num_cars - 1) // 2

    # Return the total number of ways to fill the parking lot
    return ways

