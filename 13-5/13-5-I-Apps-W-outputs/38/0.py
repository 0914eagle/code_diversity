
def solve(n, fingers):
    # Calculate the total number of fingers shown
    total_fingers = sum(fingers)
    
    # Initialize a counter for the number of ways to show fingers
    ways = 0
    
    # Loop through each possible number of fingers shown
    for i in range(1, 6):
        # Check if the current number of fingers is not equal to the total number of fingers shown
        if i != total_fingers:
            # Calculate the number of ways to show the current number of fingers
            ways += (total_fingers - i) * (i - 1)
    
    # Return the number of ways to show fingers that do not result in Dima cleaning the apartment
    return ways

