


def monotonic(l: list):
    
    # check if the list has at least two elements
    if len(l) < 2:
        return True

    # check if the list is monotonically increasing
    for i in range(len(l) - 1):
        if l[i] > l[i + 1]:
            return False

    # check if the list is monotonically decreasing
    for i in range(len(l) - 1):
        if l[i] < l[i + 1]:
            return False

    # if the list has at least two elements and is not monotonically increasing or decreasing,
    # then it must be monotonically constant
    return True


