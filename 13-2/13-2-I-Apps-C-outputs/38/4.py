
def solve(h, m, s, t_1, t_2):
    # Convert the time to a single integer
    time_1 = h * 3600 + m * 60 + s
    time_2 = t_1 * 3600 + m * 60 + s
    
    # Check if the times are the same
    if time_1 == time_2:
        return "NO"
    
    # Check if Misha can move forward or backward
    if time_1 < time_2:
        direction = 1
    else:
        direction = -1
    
    # Check if Misha can move along the clock face
    while time_1 != time_2:
        time_1 += direction * 60
        if time_1 == 0 or time_1 == 12 * 3600:
            return "NO"
    
    return "YES"

