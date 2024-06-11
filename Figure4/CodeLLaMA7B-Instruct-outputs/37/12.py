


def sort_even(l: list):
    
    l_sorted = sorted(l)
    l_even_sorted = [l[i] for i in range(0, len(l), 2)]
    l_odd_sorted = [l[i] for i in range(1, len(l), 2)]
    l_sorted.extend(l_even_sorted)
    l_sorted.extend(l_odd_sorted)
    return l_sorted


