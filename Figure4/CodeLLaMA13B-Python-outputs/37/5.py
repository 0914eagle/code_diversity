def sort_even(l: list):
    
    even_sorted = sorted(l[::2])
    even_sorted_with_odd = [None] * len(l)
    even_sorted_with_odd[::2] = even_sorted
    even_sorted_with_odd[1::2] = l[1::2]
    return even_sorted_with_odd


if __name__ == "__main__":
    import doctest

    doctest.testmod()
