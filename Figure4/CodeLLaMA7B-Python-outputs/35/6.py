def max_element(l: list):
    
    max_el = l[0]
    for i in l:
        if i > max_el:
            max_el = i
    return max_el


if __name__ == "__main__":
    import doctest

    doctest.testmod()
