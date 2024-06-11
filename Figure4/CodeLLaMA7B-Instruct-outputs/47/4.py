


def median(l: list):
    
    l.sort()
    if len(l) % 2 == 0:
        median = (l[len(l) // 2 - 1] + l[len(l) // 2]) / 2
    else:
        median = l[len(l) // 2]
    return median


# Test cases
print
