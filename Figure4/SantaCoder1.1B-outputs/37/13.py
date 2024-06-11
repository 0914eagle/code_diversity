def sort_even(l: list):
    
    l_odd = [l[i] for i in range(0, len(l), 2)]
    l_even = [l[i] for i in range(1, len(l), 2)]
    l_sorted = l_odd + l_even
    return l_sorted


