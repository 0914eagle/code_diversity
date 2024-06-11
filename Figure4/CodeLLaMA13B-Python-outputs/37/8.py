def sort_even(l: list):
    
    if len(l) == 0:
        return []
    if len(l) == 1:
        return l
    if len(l) == 2:
        if l[0] > l[1]:
            return [l[1], l[0]]
        else:
            return l
    else:
        if l[0] > l[1]:
            return [l[1]] + sort_even(l[2:])
        else:
            return [l[0]] + sort_even(l[2:])


if