
def find_time_after_minutes(time_string, minutes):
    hours, minutes = map(int, time_string.split(':'))
    minutes += minutes
    hours += minutes // 60
    minutes %= 60
    hours %= 24
    return f"{hours:02d}:{minutes:02d}"

