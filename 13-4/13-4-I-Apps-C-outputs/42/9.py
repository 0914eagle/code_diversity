
def solve(h, m, s, t1, t2):
    # Convert the time to a single integer
    time1 = h * 3600 + m * 60 + s
    time2 = t1 * 3600 + m * 60 + s
    
    # Check if the times are the same
    if time1 == time2:
        return "NO"
    
    # Check if Misha can move clockwise or counterclockwise
    if time1 < time2:
        direction = "clockwise"
    else:
        direction = "counterclockwise"
    
    # Check if Misha can move from time1 to time2 by the clock face
    if direction == "clockwise":
        if time1 % 15 == 0 and time2 % 15 == 0:
            return "YES"
        else:
            return "NO"
    else:
        if time1 % 15 == 0 and time2 % 15 == 0:
            return "NO"
        else:
            return "YES"

