def pairs_sum_to_zero(l):
    
    # create a set of the list
    s = set(l)
    # iterate over the set
    for i in s:
        # check if the complement of i is in the set
        if (-i in s):
            return True
    return False


if __name__ == "__main__":
    import doctest
    doctest.testmod()
