


def monotonic(l: list):
    
    # Check if the list has at least two elements
    if len(l) < 2:
        return True

    # Check if the list is monotonically increasing
    for i in range(len(l) - 1):
        if l[i] > l[i + 1]:
            return False

    # Check if the list is monotonically decreasing
    for i in range(len(l) - 1):
        if l[i] < l[i + 1]:
            return False

    # If the list has at least two elements and is not monotonically increasing or decreasing,
    # then it must be constant
    return True


