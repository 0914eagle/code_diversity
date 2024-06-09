
def get_midpoint(start_time, end_time):
    hours_1, minutes_1 = map(int, start_time.split(':'))
    hours_2, minutes_2 = map(int, end_time.split(':'))
    total_minutes = (hours_2 - hours_1) * 60 + (minutes_2 - minutes_1)
    midpoint_minutes = total_minutes // 2
    hours_3 = hours_1 + midpoint_minutes // 60
    minutes_3 = midpoint_minutes % 60
    return f"{hours_3:02d}:{minutes_3:02d}"

