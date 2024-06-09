
def car_race_collision(n: int) -> int:
    
    # Initialize the number of collisions to 0
    collisions = 0

    # Loop through each car in the left-to-right set
    for i in range(n):
        # Loop through each car in the right-to-left set
        for j in range(n):
            # Check if the cars are at the same position
            if i == j:
                # Increment the number of collisions
                collisions += 1

    # Return the number of collisions
    return collisions

