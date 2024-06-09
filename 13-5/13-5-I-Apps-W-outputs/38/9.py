
def solve(n, fingers):
    # Calculate the total number of fingers shown
    total_fingers = sum(fingers)
    
    # Initialize a counter for the number of ways to show fingers
    ways = 0
    
    # Loop through each finger combination
    for i in range(1, 6):
        # Check if the total number of fingers shown is divisible by the current finger combination
        if total_fingers % i == 0:
            # Increment the counter
            ways += 1
    
    # Return the number of ways to show fingers
    return ways

