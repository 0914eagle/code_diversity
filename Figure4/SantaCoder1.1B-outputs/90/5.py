def next_smallest(lst):
    
    if not lst:
        return None
    if len(lst) == 1:
        return lst[0]
    if len(lst) == 2:
        return min(lst) if lst[0] < lst[1] else max(lst)
    if len(lst) == 3:
        return min(lst) if lst[0] < lst[1] < lst[2] else max(lst)
    if len(lst) == 4:
        return min(lst) if lst[0] < lst[1] < lst[2] < lst[3] else max(lst)
    if len(lst) == 5:
        return min(lst) if lst[0] < lst[1] < lst[2] < lst[3] < lst[4] else max(lst)
    if len(lst) == 6:
        return min(lst) if lst[0] < lst[1] < lst[2] < lst[3] < lst[4] < lst[5] else max(lst)
    if len(lst) == 7:
        return min(lst) if lst[0] < lst[1] < lst[2] < lst[3] < lst[4] < lst[5] < lst[6] else max(lst)
    if len(lst) == 8:
        return min(lst) if lst[0] < lst[1] < lst[2] < lst[3] < lst[4] < lst[5] < lst[6] < lst[7] else max(lst)
    if len(lst) == 9:
        return min(lst) if lst[0] < lst[1] < lst[2] < lst[3] < lst[4] < lst[5] < lst[6] < lst[7] < lst[8] else max(lst)
    if len(lst) == 10:
        return min(lst) if lst[0] < lst[1] < lst[2] < lst[3] < lst[4] < lst[5] < lst[6] < lst[7] < lst[8] < lst[9] else max(lst)
    return None


