
def solve(n):
    # Calculate the number of special points
    num_special_points = (n * (n + 1)) // 2
    
    # Initialize the number of blocked points to 0
    num_blocked_points = 0
    
    # Loop through each special point
    for i in range(1, num_special_points + 1):
        # Calculate the distance from the origin
        distance = i
        
        # Check if the distance is a perfect square
        if is_perfect_square(distance):
            # Increment the number of blocked points
            num_blocked_points += 1
    
    # Return the minimum number of blocked points needed
    return num_blocked_points

def is_perfect_square(n):
    # Calculate the square root of the number
    sqrt = int(n ** 0.5)
    
    # Check if the square root is a whole number
    return sqrt ** 2 == n

