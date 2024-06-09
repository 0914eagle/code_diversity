
def solve(n):
    # Calculate the number of special points
    num_special_points = (n * (n + 1)) // 2
    
    # Calculate the minimum number of blocked points needed
    num_blocked_points = num_special_points - 1
    
    return num_blocked_points

