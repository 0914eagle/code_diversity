
def cook_chicken(k, d, t):
    total_time = 0
    while total_time < t:
        stove_on_time = min(t - total_time, k)
        total_time += stove_on_time
        total_time += (stove_on_time / t) * d
    return total_time
