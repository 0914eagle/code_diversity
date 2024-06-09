
def get_max_vegetables(lanes, capacity):
    # Sort the lanes by the day they become edible
    sorted_lanes = sorted(lanes, key=lambda x: x[0])

    # Initialize variables to keep track of the number of vegetables collected and the current day
    total_vegetables = 0
    current_day = 1

    # Loop through the lanes and collect vegetables until the capacity is reached or there are no more lanes to collect from
    while total_vegetables < capacity and sorted_lanes:
        # Get the next lane with vegetables that become edible on the current day
        next_lane = next((lane for lane in sorted_lanes if lane[0] == current_day), None)

        # If there are no more lanes with vegetables that become edible on the current day, move on to the next day
        if not next_lane:
            current_day += 1
            continue

        # Remove the lane from the list of lanes and add the number of vegetables to the total
        total_vegetables += next_lane[1]
        sorted_lanes.remove(next_lane)

    return total_vegetables

