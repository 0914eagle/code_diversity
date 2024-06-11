def sort_third(l: list):
    
    l_sorted = sorted(l[::3])
    l_sorted_with_third = [l_sorted[i // 3] if i % 3 == 0 else l[i] for i in range(len(l))]
    return l_sorted_with_third


if