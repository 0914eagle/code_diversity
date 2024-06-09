
def car_race_collision(n: int) -> int:
    
    # Initialize the number of collisions to 0
    collisions = 0

    # Loop through each pair of cars
    for i in range(n):
        # If the cars are moving in the same direction (i.e. not colliding)
        if i % 2 == 0:
            # Increment the number of collisions
            collisions += 1

    # Return the number of collisions
    return collisions

