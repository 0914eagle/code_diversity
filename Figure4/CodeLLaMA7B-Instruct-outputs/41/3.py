


def car_race_collision(n: int):
    
    # Initialize the number of collisions to 0
    collisions = 0

    # Loop through the range of the number of cars
    for i in range(n):
        # If the cars are in the same position, they have collided
        if i % 2 == 0:
            collisions += 1

    # Return the number of collisions
    return collisions


# Test the function with different
