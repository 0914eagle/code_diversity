


def triples_sum_to_zero(l: list):
    

    # check if the list has at least three elements
    if len(l) < 3:
        return False

    # sort the list
    l.sort()

    # check if any three elements sum to zero
    for i in range(len(l) - 2):
        if l[i] + l[i + 1] + l[i + 2] == 0:
            return True

    # if no three elements sum to zero, return False
    return False


