
def worm_climbing(a, b, h):
    times = 0
    while h > 0:
        h = h - a
        times += 1
        h = h - b
    return times

