def sort_even(l: list):
    
    l_even = l[::2]
    l_even.sort()
    l_odd = l[1::2]
    return l_even + l_odd


