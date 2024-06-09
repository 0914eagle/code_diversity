
def find_time_after_minutes(time, minutes):
    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes)
    minutes += int(minutes)
    hours += int(minutes) // 60
    minutes %= 60
    return f"{hours:02d}:{minutes:02d}"

