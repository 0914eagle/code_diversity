


def sort_even(l: list):
    
    l_sorted = sorted(l)
    l_even = [l[i] for i in range(0, len(l), 2)]
    l_odd = [l[i] for i in range(1, len(l), 2)]
    l_sorted_even = sorted(l_even)
    l_sorted_odd = l_odd
    l_sorted_even.reverse()
    l_sorted_odd.reverse()
    l_sorted_even.extend(l_sorted_odd)
    return l_sorted_even



