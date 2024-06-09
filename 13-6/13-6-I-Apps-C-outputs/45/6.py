
def get_total_time(k, d, t):
    total_time = 0
    while total_time < t:
        if total_time % (2 * t) < t:
            total_time += min(k, t - total_time)
        else:
            total_time += min(k, t - total_time) + d
    return total_time

