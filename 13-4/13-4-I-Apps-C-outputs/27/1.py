
def cook_chicken(k, d, t):
    total_time = 0
    stove_on = False
    while total_time < t:
        if stove_on:
            total_time += t
        else:
            total_time += 2 * t
        stove_on = not stove_on
        total_time += d
    return total_time

