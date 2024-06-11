


def car_race_collision(n: int):
    
    # Initialize the number of collisions to 0
    collisions = 0

    # Loop through the cars moving left to right
    for i in range(n):
        # Loop through the cars moving right to left
        for j in range(n):
            # Check if the cars are in the same lane and have not collided yet
            if i != j and abs(i - j) <= 1:
                # Increment the number of collisions
                collisions += 1

    # Return the number of collisions
    return collisions


#
