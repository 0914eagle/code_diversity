def sort_even(l: list):
    
    even_sorted = sorted(l[::2])
    odd_sorted = l[1::2]
    return [odd_sorted[i] if i < len(odd_sorted) else even_sorted[i] for i in range(len(l))]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
