
def get_total_time(k, d, t):
    total_time = 0
    while total_time < t:
        if total_time % (k + d) < k:
            total_time += t / k
        else:
            total_time += t / (k + d)
    return total_time

