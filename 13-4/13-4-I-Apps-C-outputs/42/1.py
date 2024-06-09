
def solve(h, m, s, t_1, t_2):
    # Convert the time to a single integer
    time_1 = h * 3600 + m * 60 + s
    time_2 = t_1 * 3600 + m * 60 + s
    
    # Check if the times are equal
    if time_1 == time_2:
        return "NO"
    
    # Check if the times are within the same hour
    if time_1 // 3600 == time_2 // 3600:
        return "YES"
    
    # Check if the times are within the same minute
    if time_1 // 60 == time_2 // 60:
        return "YES"
    
    # Check if the times are within the same second
    if time_1 == time_2:
        return "YES"
    
    # Check if the times are within the same hour and minute
    if time_1 // 3600 == time_2 // 3600 and time_1 // 60 == time_2 // 60:
        return "YES"
    
    # Check if the times are within the same hour and second
    if time_1 // 3600 == time_2 // 3600 and time_1 == time_2:
        return "YES"
    
    # Check if the times are within the same minute and second
    if time_1 // 60 == time_2 // 60 and time_1 == time_2:
        return "YES"
    
    # If none of the above conditions are met, return "NO"
    return "NO"

