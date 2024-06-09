
def solve(format, time):
    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes)
    
    if format == "12":
        if hours > 12:
            hours = hours - 12
        if hours == 0:
            hours = 12
        if minutes > 59:
            minutes = minutes - 60
        if minutes < 10:
            minutes = "0" + str(minutes)
        return f"{hours}:{minutes}"
    else:
        if hours > 23:
            hours = hours - 24
        if hours < 10:
            hours = "0" + str(hours)
        if minutes > 59:
            minutes = minutes - 60
        if minutes < 10:
            minutes = "0" + str(minutes)
        return f"{hours}:{minutes}"

