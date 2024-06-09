
def get_midpoint(start_time, end_time):
    start_h, start_m = map(int, start_time.split(':'))
    end_h, end_m = map(int, end_time.split(':'))
    total_minutes = (end_h - start_h) * 60 + (end_m - start_m)
    midpoint_minutes = total_minutes // 2
    midpoint_h = start_h + midpoint_minutes // 60
    midpoint_m = midpoint_minutes % 60
    return f"{midpoint_h:02d}:{midpoint_m:02d}"

