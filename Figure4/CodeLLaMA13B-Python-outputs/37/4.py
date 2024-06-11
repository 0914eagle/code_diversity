def sort_even(l: list):
    
    if len(l) == 0:
        return []
    if len(l) == 1:
        return l
    if len(l) == 2:
        if l[0] > l[1]:
            return [l[1], l[0]]
        return l
    if len(l) > 2:
        if l[0] > l[1]:
            return [l[1], l[0]] + sort_even(l[2:])
        return [l[0]] + sort_even(l[1:])


if __name__ == "__