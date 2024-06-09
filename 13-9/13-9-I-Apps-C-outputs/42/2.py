
def is_divisibility_hack_valid(b, d):
    if b == d:
        return "no"
    if b % d == 0:
        return "no"
    for m in range(1, b):
        if (b ** m - 1) % d == 0:
            return "yes"
    return "no"

