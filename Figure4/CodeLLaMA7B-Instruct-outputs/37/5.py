


def sort_even(l: list):
    
    l_sorted = sorted(l)
    l_even_sorted = []
    for i in range(0, len(l), 2):
        l_even_sorted.append(l_sorted[i])
    for i in range(1, len(l), 2):
        l_even_sorted.append(l[i])
    return l_even_sorted


