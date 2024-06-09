
def solve(n):
    # Calculate the number of special points
    num_special_points = (n * (n + 1)) // 2
    
    # Initialize the number of blocked points to 0
    num_blocked_points = 0
    
    # Iterate through all possible combinations of blocked points
    for i in range(num_special_points):
        # Calculate the number of blocked points needed for this combination
        num_blocked_points_needed = num_special_points - i
        
        # Check if this is the minimum number of blocked points needed
        if num_blocked_points_needed > num_blocked_points:
            num_blocked_points = num_blocked_points_needed
    
    return num_blocked_points

