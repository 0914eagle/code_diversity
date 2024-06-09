
def get_maximum_vegetables(lanes, capacity):
    # Sort the lanes based on the number of vegetables in each lane
    lanes.sort(key=lambda x: x[1], reverse=True)
    # Initialize variables to keep track of the number of vegetables collected and the current day
    total_vegetables = 0
    current_day = 1
    # Loop through each lane and collect vegetables if they are edible on the current day
    for lane in lanes:
        if lane[0] <= current_day:
            total_vegetables += min(lane[1], capacity)
            current_day += 1
    return total_vegetables

