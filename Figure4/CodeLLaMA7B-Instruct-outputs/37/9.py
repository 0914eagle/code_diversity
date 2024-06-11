


def sort_even(l: list):
    
    l_sorted = sorted(l)
    l_even = [l[i] for i in range(0, len(l), 2)]
    l_odd = [l[i] for i in range(1, len(l), 2)]
    l_sorted_even = sorted(l_even)
    return [x for i, x in enumerate(l_odd) if i % 2 == 0] + l_sorted_even


