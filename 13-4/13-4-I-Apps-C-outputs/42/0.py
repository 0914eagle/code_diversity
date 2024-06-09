
def can_prepare_contest(h, m, s, t_1, t_2):
    # Convert the time to total seconds
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
    
    # Check if the times are within the same hour but on opposite sides of the clock
    if (time_1 // 3600 == time_2 // 3600) and (time_1 % 3600 != time_2 % 3600):
        return "YES"
    
    # Check if the times are within the same minute but on opposite sides of the clock
    if (time_1 // 60 == time_2 // 60) and (time_1 % 60 != time_2 % 60):
        return "YES"
    
    # Check if the times are within the same second but on opposite sides of the clock
    if (time_1 == time_2) and (time_1 != time_2):
        return "YES"
    
    # If none of the above conditions are met, the contest cannot be prepared on time
    return "NO"

