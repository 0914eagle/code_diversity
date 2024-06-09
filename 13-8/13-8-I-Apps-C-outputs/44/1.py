
def solve(n):
    # Calculate the number of special points
    num_special_points = (n * (n + 1)) // 2
    
    # Initialize the minimum number of points to block as the number of special points
    min_points_to_block = num_special_points
    
    # Iterate through all possible combinations of blocked points
    for i in range(1, num_special_points + 1):
        # Calculate the number of non-special points that are 4-connected to a special point
        num_non_special_points = num_special_points - i
        
        # If the number of non-special points is less than or equal to the number of special points,
        # we have found a valid combination where no special point is 4-connected to a non-special point
        if num_non_special_points <= num_special_points:
            min_points_to_block = min(min_points_to_block, i)
    
    return min_points_to_block

