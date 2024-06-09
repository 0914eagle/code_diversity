
def car_race_collision(n: int) -> int:
    
    # Initialize the number of collisions to 0
    collisions = 0
    
    # Loop through each pair of cars
    for i in range(n):
        # Check if the cars are on the same position
        if i == n - i - 1:
            # Increment the number of collisions
            collisions += 1
    
    # Return the number of collisions
    return collisions

