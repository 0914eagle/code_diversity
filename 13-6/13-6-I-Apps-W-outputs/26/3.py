
def get_max_vegetables(num_lanes, capacity, lanes):
    # Sort the lanes by their day of harvest in ascending order
    sorted_lanes = sorted(lanes, key=lambda x: x[0])

    # Initialize variables to keep track of the number of vegetables collected and the current day
    total_vegetables = 0
    current_day = 1

    # Loop through the lanes and collect vegetables on the days when they are harvested
    for lane in sorted_lanes:
        while current_day <= lane[0] and total_vegetables + lane[1] <= capacity:
            total_vegetables += lane[1]
            current_day += 1

    return total_vegetables

