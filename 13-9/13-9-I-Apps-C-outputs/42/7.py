
def is_divisibility_hack_valid(b, d):
    if b == d:
        return "no"
    if b % d == 0:
        return "no"
    if d == 2:
        return "yes"
    for m in range(1, b):
        if (b - 1) % m == 0 and (d - 1) % m == 0:
            return "yes"
    return "no"

