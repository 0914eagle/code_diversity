
def get_maximum_vegetables(m, v, days, lanes):
    # Sort the lanes based on the day they become edible
    sorted_lanes = sorted(lanes, key=lambda x: x[0])

    # Initialize the variables
    total_vegetables = 0
    current_day = 1

    # Loop through the lanes and collect vegetables
    for lane in sorted_lanes:
        # Check if the lane becomes edible on the current day
        if lane[0] == current_day:
            # Check if the number of vegetables in the lane is less than or equal to the capacity
            if lane[1] <= v:
                # Add the number of vegetables to the total
                total_vegetables += lane[1]
            # Else, add the capacity to the total
            else:
                total_vegetables += v

        # Increment the current day
        current_day += 1

    # Return the total number of vegetables collected
    return total_vegetables

