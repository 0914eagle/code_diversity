


def car_race_collision(n: int):
    
    # Initialize the number of collisions to 0
    collisions = 0

    # Loop through the cars on the left and right sides
    for i in range(n):
        # If the cars on the left and right sides are at the same position,
        # they have collided
        if i == n - i - 1:
            collisions += 1

    # Return the number of collisions
    return collisions


#
