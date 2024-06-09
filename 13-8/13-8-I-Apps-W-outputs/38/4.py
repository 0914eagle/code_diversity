
def find_time(time_str, minutes):
    hours, minutes = map(int, time_str.split(':'))
    minutes += minutes
    hours += minutes // 60
    minutes %= 60
    return f"{hours:02d}:{minutes:02d}"

