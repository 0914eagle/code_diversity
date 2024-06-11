


def triples_sum_to_zero(l: list):
    

    # check if the list has three or more elements
    if len(l) < 3:
        return False

    # sort the list
    l.sort()

    # loop through the list and find three distinct elements that sum to zero
    for i in range(len(l) - 2):
        a = l[i]
        for j in range(i + 1, len(l) - 1):
            b = l[j]
            for k in range(j + 1, len(l)):
                c = l[k]
                if a + b + c == 0 and a != b and b != c and a != c:
                    return True

    # if no three distinct elements are found, return False
    return False


