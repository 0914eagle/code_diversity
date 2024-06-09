
def find_time_after_minutes(time, minutes):
    hours, minutes = map(int, time.split(':'))
    minutes += minutes
    hours += minutes // 60
    minutes %= 60
    return f"{hours:02d}:{minutes:02d}"

