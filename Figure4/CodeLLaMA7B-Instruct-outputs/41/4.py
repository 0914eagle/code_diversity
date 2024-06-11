


def car_race_collision(n: int):
    
    # Initialize the number of collisions to 0
    collisions = 0

    # Loop through the range of the number of cars
    for i in range(n):
        # Check if the cars have collided
        if i % 2 == 0:
            # If the cars have collided, increment the number of collisions
            collisions += 1

    # Return the number of collisions
    return collisions


#
