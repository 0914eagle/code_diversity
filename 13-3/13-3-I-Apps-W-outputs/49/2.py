
def get_min_staircases(n, s, k, closed_floors):
    # Initialize the minimum number of staircases to walk as 0
    min_staircases = 0

    # If all restaurants are closed, return -1
    if k == n:
        return -1

    # If ConneR's office has an open restaurant, return 0
    if s in closed_floors:
        return 0

    # Initialize the current floor as ConneR's office floor
    current_floor = s

    # Loop through the closed floors
    for floor in closed_floors:
        # If the current floor is higher than the closed floor, increase the minimum number of staircases
        if current_floor > floor:
            min_staircases += 1
        # If the current floor is lower than the closed floor, decrease the minimum number of staircases
        elif current_floor < floor:
            min_staircases -= 1
        # If the current floor is equal to the closed floor, do nothing
        else:
            pass

        # Update the current floor to the next floor
        current_floor += 1

    # Return the minimum number of staircases
    return min_staircases

