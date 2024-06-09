
def is_possible(n, t, time_periods):
    time_periods.sort(key=lambda x: x[0])
    current_time = 0
    for i in range(n):
        start_time, end_time = time_periods[i]
        if current_time + t > start_time:
            return "no"
        current_time = max(current_time + t, end_time)
    return "yes"

