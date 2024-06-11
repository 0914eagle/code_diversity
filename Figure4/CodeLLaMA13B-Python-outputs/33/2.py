def sort_third(l: list):
    
    l_sorted = sorted(l[::3])
    l_sorted_repeated = []
    for i in range(len(l) // 3):
        l_sorted_repeated.extend([l_sorted[i]] * 3)
    return [l[i] if i % 3 != 0 else l_sorted_repeated[i // 3] for i in range(len(l))]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
