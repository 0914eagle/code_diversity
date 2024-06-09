
def worm_problem(a, b, h):
    count = 0
    while h > 0:
        h = h - a
        if h < b:
            return count + 1
        h = h - b
        count += 1
    return count

