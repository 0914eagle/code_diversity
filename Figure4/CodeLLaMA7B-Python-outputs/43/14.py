def pairs_sum_to_zero(l):
    
    seen = set()
    for num in l:
        if num in seen:
            return True
        seen.add(-num)
    return False


if __name__ == "__main__":
    import doctest

    doctest.testmod()
