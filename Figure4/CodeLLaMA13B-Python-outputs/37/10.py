def sort_even(l: list):
    
    even_sorted = sorted(l[::2])
    odd_sorted = l[1::2]
    return [x for t in zip(even_sorted, odd_sorted) for x in t]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
