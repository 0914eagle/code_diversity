
def get_time_to_cook(k, d, t):
    total_time = 0
    while total_time < t:
        if total_time % (k + d) < k:
            total_time += t / (k + d)
        else:
            total_time += 2 * t / (k + d)
    return total_time

