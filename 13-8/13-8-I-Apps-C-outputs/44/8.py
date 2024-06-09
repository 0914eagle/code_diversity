
def solve(n):
    # Calculate the number of special points
    num_special_points = (n * (n + 1)) // 2
    
    # Calculate the minimum number of blocked points needed to achieve the property
    min_blocked_points = num_special_points - 1
    
    return min_blocked_points

