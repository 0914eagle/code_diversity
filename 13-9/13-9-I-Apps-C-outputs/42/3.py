
def divisibility_hack(b, d):
    for m in range(1, b):
        if pow(b, m, d) == 1:
            return "yes"
    return "no"

