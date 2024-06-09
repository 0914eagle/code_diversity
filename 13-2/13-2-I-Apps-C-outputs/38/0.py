
def solve(h, m, s, t1, t2):
    # Convert the time to a single number
    time1 = h * 3600 + m * 60 + s
    time2 = t1 * 3600 + m * 60 + s
    
    # Check if the times are the same
    if time1 == time2:
        return "NO"
    
    # Check if Misha can move forward or backward
    if time1 < time2:
        direction = 1
    else:
        direction = -1
    
    # Check if Misha can move along the clock face
    while time1 != time2:
        time1 += direction * 60
        if time1 == 0 or time1 == 24 * 3600:
            return "NO"
    
    return "YES"

