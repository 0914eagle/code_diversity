
def get_max_vegetables(lanes, capacity):
    # Sort the lanes based on the number of vegetables in each lane
    sorted_lanes = sorted(lanes, key=lambda x: x[1], reverse=True)

    # Initialize variables to keep track of the number of vegetables collected and the current day
    total_vegetables = 0
    current_day = 1

    # Loop through the lanes and collect vegetables until the capacity is reached or there are no more lanes with edible vegetables
    while total_vegetables < capacity and sorted_lanes:
        # Find the first lane with edible vegetables and collect as many as possible
        for lane in sorted_lanes:
            if lane[0] <= current_day:
                total_vegetables += min(lane[1], capacity - total_vegetables)
                lane[1] -= min(lane[1], capacity - total_vegetables)

        # Increment the current day and remove any lanes with 0 vegetables
        current_day += 1
        sorted_lanes = [lane for lane in sorted_lanes if lane[1] > 0]

    return total_vegetables

