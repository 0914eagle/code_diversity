
def solve(h, m, s, t_1, t_2):
    # Convert the time to a single integer
    time_1 = h * 3600 + m * 60 + s
    time_2 = t_1 * 3600 + t_2 * 60
    
    # Check if the times are equal
    if time_1 == time_2:
        return "NO"
    
    # Check if Misha can move clockwise or counterclockwise
    if time_1 < time_2:
        direction = 1
    else:
        direction = -1
    
    # Check if Misha can move along the top arc
    if time_1 + direction == time_2:
        return "YES"
    
    # Check if Misha can move along the bottom arc
    if time_1 - direction == time_2:
        return "YES"
    
    # Check if Misha can move along the left arc
    if time_1 - 3600 == time_2:
        return "YES"
    
    # Check if Misha can move along the right arc
    if time_1 + 3600 == time_2:
        return "YES"
    
    # If Misha cannot move to the target time, return "NO"
    return "NO"

