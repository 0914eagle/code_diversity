
def find_time(time_str, minutes):
    hours, minutes = time_str.split(":")
    hours = int(hours)
    minutes = int(minutes)
    minutes += minutes
    hours += minutes // 60
    minutes %= 60
    return f"{hours:02d}:{minutes:02d}"

