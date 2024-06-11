def pairs_sum_to_zero(l):
    
    # make a set of the list
    s = set(l)
    # check if the sum of any two elements is zero
    for i in l:
        if i == 0:
            if l.count(i) > 1:
                return True
        else:
            if -(i) in s:
                return True
    return False


if __name__ == "__main__":
    import doctest

    doctest.testmod()
