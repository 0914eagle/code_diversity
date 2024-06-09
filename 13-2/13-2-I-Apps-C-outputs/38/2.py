
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
    
    # Check if Misha can move along the hour hand
    if (time1 // 3600) % 12 == (time2 // 3600) % 12:
        return "NO"
    
    # Check if Misha can move along the minute hand
    if (time1 // 60) % 60 == (time2 // 60) % 60:
        return "NO"
    
    # Check if Misha can move along the second hand
    if time1 % 60 == time2 % 60:
        return "NO"
    
    # Misha can move along the hour hand
    if (time1 // 3600) % 12 != (time2 // 3600) % 12:
        return "YES"
    
    # Misha can move along the minute hand
    if (time1 // 60) % 60 != (time2 // 60) % 60:
        return "YES"
    
    # Misha can move along the second hand
    if time1 % 60 != time2 % 60:
        return "YES"
    
    return "NO"

