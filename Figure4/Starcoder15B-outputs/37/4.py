def sort_even(l: list):
    
    l_even = l[::2]
    l_even.sort()
    l_odd = l[1::2]
    return [x for pair in zip(l_even, l_odd) for x in pair]


