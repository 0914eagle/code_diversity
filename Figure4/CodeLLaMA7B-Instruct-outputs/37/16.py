


def sort_even(l: list):
    
    l_sorted = sorted(l)
    l_even_sorted = [l[i] for i in range(0, len(l), 2)]
    l_odd = [l[i] for i in range(1, len(l), 2)]
    l_even = [l_sorted[i] for i in range(0, len(l), 2)]
    l_even_sorted.extend(l_odd)
    l_even_sorted.extend(l_odd)
    return l_even_sorted


