
def get_new_time(clock_change):
    # Initialize variables
    roll_forward, minutes_changed, hour, minute = clock_change

    # Calculate the new time
    new_hour = hour + int(minutes_changed / 60)
    new_minute = minute + (minutes_changed % 60)

    # Handle rollover
    if roll_forward == "F":
        if new_hour == 24:
            new_hour = 0
    else:
        if new_hour == -1:
            new_hour = 23

    # Return the new time
    return f"{new_hour:02d} {new_minute:02d}"

