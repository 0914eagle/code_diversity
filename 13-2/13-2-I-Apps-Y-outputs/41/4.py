
def get_new_time(clock_change):
    # Initialize variables
    roll_forward, minutes_changed, hour, minute = clock_change

    # Calculate the new time
    if roll_forward == "F":
        minute = (minute + minutes_changed) % 60
        hour = (hour + int(minute / 60)) % 24
    else:
        minute = (minute - minutes_changed) % 60
        hour = (hour - int(minute / 60)) % 24

    # Return the new time
    return f"{hour:02d} {minute:02d}"

