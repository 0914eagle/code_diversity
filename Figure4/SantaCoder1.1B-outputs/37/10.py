def sort_even(l: list):
    
    l_odd = [x for i, x in enumerate(l) if i % 2 == 1]
    l_even = [x for i, x in enumerate(l) if i % 2 == 0]
    l_odd.sort()
    l_even.sort()
    l_sorted = l_odd + l_even
    return l_sorted


