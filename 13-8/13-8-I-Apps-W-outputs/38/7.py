
def print_time_after_minutes(time, minutes):
    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes)
    total_minutes = (hours * 60) + minutes + minutes
    hours = total_minutes // 60
    minutes = total_minutes % 60
    return f"{hours:02d}:{minutes:02d}"

