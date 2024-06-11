def pairs_sum_to_zero(l):
    
    # make a set of the list
    l_set = set(l)
    # make a set of the sums of all pairs
    l_sums = set()
    for i in l:
        l_sums.add(sum([i, -i]))
    # return True if the sum of all pairs is in the set of the list
    return l_sums.issubset(l_set)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
