
def solve(N, clock_direction, minutes_to_change, hour, minute):
    if clock_direction == "F":
        new_hour = hour + minutes_to_change // 60
        new_minute = minute + minutes_to_change % 60
    else:
        new_hour = hour - minutes_to_change // 60
        new_minute = minute - minutes_to_change % 60
    
    if new_hour > 23:
        new_hour = new_hour - 24
    
    if new_minute < 0:
        new_minute = new_minute + 60
    
    return f"{new_hour:02d} {new_minute:02d}"

