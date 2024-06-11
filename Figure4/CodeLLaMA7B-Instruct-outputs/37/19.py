


def sort_even(l: list):
    
    l_sorted = sorted(l)
    l_even_sorted = [l_sorted[i] for i in range(0, len(l), 2)]
    l_odd = [l[i] for i in range(1, len(l), 2)]
    return l_even_sorted + l_odd


