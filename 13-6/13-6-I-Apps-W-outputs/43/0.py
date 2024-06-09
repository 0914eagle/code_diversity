
def count_ways(n):
    # Initialize a list to store the number of ways to fill the parking lot
    ways = [0] * (n + 1)

    # Base case: when n is 1, there is only one way to fill the parking lot
    ways[1] = 1

    # Iterate from 2 to n
    for i in range(2, n + 1):
        # Initialize a variable to store the number of ways to fill the parking lot
        total_ways = 0

        # Iterate over the four car makes
        for make in ["A", "B", "M", "Z"]:
            # Calculate the number of ways to fill the parking lot with the current make
            make_ways = ways[i - 1]

            # Add the number of ways to fill the parking lot with the current make to the total number of ways
            total_ways += make_ways

        # Store the total number of ways in the list
        ways[i] = total_ways

    # Return the total number of ways to fill the parking lot
    return ways[n]

