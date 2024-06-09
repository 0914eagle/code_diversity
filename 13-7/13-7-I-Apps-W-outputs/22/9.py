
def solve(n, m, building):
    # Initialize the minimum time variable
    min_time = 0

    # Loop through each floor
    for floor in range(n):
        # Get the current floor string
        floor_string = building[floor]

        # Find the index of the first '1' in the floor string
        first_on_index = floor_string.index('1')

        # Calculate the time it takes to get to the first on light
        time_to_first_on = first_on_index * 2

        # Add the time it takes to turn off the light
        min_time += time_to_first_on + 1

        # Find the index of the last '1' in the floor string
        last_on_index = floor_string.rindex('1')

        # Calculate the time it takes to get to the last on light
        time_to_last_on = (m - last_on_index) * 2

        # Add the time it takes to turn off the light
        min_time += time_to_last_on + 1

    # Return the minimum time
    return min_time

