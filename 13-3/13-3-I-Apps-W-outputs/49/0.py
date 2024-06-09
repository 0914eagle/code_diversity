
def get_min_staircases(n, s, k, closed_floors):
    # Initialize the minimum number of staircases to walk as 0
    min_staircases = 0

    # Loop through the closed floors and check if the current floor is one of them
    for floor in closed_floors:
        # If the current floor is one of the closed floors, increment the minimum number of staircases
        if floor == s:
            min_staircases += 1
        # If the current floor is between the current floor and the next closed floor, increment the minimum number of staircases
        elif floor > s and floor < closed_floors[closed_floors.index(floor) + 1]:
            min_staircases += 1

    return min_staircases

