def pairs_sum_to_zero(l):
    
    # return True if there are two distinct elements in the list that sum to zero
    # return False otherwise
    if len(l) < 2:
        return False
    else:
        for i in range(len(l)):
            for j in range(i + 1, len(l)):
                if l[i] + l[j] == 0:
                    return True
        return False


if __name__ == "__main__":
    import doctest
    doctest.testmod()
