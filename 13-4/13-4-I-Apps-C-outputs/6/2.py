
def get_number_of_ways(snow_log):
    # Initialize variables
    num_ways = 0
    max_snow_level = 0
    min_snow_level = 0
    previous_snow_level = 0

    # Iterate through the snow log
    for snow_range in snow_log:
        # Get the snow level for the current range
        current_snow_level = snow_range[1] - snow_range[0] + 1

        # Check if the current snow level is higher than the previous snow level
        if current_snow_level > previous_snow_level:
            # Increment the number of ways
            num_ways += 1

            # Update the maximum snow level
            max_snow_level = max(max_snow_level, current_snow_level)

        # Check if the current snow level is lower than the previous snow level
        elif current_snow_level < previous_snow_level:
            # Update the minimum snow level
            min_snow_level = min(min_snow_level, current_snow_level)

        # Update the previous snow level
        previous_snow_level = current_snow_level

    # Check if the minimum snow level is greater than the maximum snow level
    if min_snow_level > max_snow_level:
        return "shovel time!"

    # Return the number of ways
    return num_ways % 1000000009

