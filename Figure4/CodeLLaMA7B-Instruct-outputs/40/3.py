


def triples_sum_to_zero(l: list):
    

    # check if the list has three or more elements
    if len(l) < 3:
        return False

    # sort the list
    l.sort()

    # loop through the list
    for i in range(len(l) - 2):
        # check if the sum of the first two elements is equal to the third element
        if l[i] + l[i + 1] == l[i + 2]:
            return True

    # if no three distinct elements sum to zero, return False
    return False


