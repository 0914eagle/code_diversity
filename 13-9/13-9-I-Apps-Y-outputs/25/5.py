
def worm_climbing(a, b, h):
    count = 0
    while h > 0:
        h = h - a
        count += 1
        if h > 0:
            h = h - b
    return count

