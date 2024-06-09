
def get_max_vegetables(m, v, d, a):
    # Sort the lanes based on the day they become edible
    sorted_lanes = sorted(zip(d, a), key=lambda x: x[0])

    # Initialize the variables
    total_vegetables = 0
    current_day = 1
    collected_vegetables = 0

    # Loop through the lanes
    for i in range(m):
        # Check if the current day is within the range of the current lane
        if current_day >= sorted_lanes[i][0] and current_day <= sorted_lanes[i][0] + 1:
            # Check if the collected vegetables are less than the capacity
            if collected_vegetables < v:
                # Add the vegetables to the total and increase the collected vegetables
                total_vegetables += sorted_lanes[i][1]
                collected_vegetables += sorted_lanes[i][1]
            # If the collected vegetables are greater than the capacity, then break the loop
            else:
                break

        # Increase the current day
        current_day += 1

    return total_vegetables

