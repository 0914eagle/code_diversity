
def solve(h, m, s, t1, t2):
    # Convert the time to a single integer
    time1 = h * 3600 + m * 60 + s
    time2 = t1 * 3600 + m * 60 + s
    
    # Check if the times are equal
    if time1 == time2:
        return "NO"
    
    # Check if Misha can move forward or backward
    if time1 < time2:
        direction = 1
    else:
        direction = -1
    
    # Check if Misha can move along the top arc
    if (time1 + direction) % 12 == t2:
        return "YES"
    
    # Check if Misha can move along the bottom arc
    if (time1 + direction) % 12 == t2 - 12:
        return "YES"
    
    # Check if Misha can move along the left arc
    if (time1 + direction) % 12 == t2 - 1:
        return "YES"
    
    # Check if Misha can move along the right arc
    if (time1 + direction) % 12 == t2 + 1:
        return "YES"
    
    # If Misha cannot move along any arc, return "NO"
    return "NO"

