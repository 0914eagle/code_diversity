def next_smallest(lst):
    
    if not lst:
        return None
    if len(lst) == 1:
        return lst[0]
    if len(lst) == 2:
        return min(lst)
    if len(lst) == 3:
        return min(lst) if lst[0] < lst[1] else lst[1]
    if len(lst) == 4:
        return min(lst) if lst[0] < lst[1] else min(lst) if lst[1] < lst[2] else lst[2]
    if len(lst) == 5:
        return min(lst) if lst[0] < lst[1] else min(lst) if lst[1] < lst[2] else min(lst) if lst[2] < lst[3] else lst[3]
    if len(lst) == 6:
        return min(lst) if lst[0] < lst[1] else min(lst) if lst[1] < lst[2] else min(lst) if lst[2] < lst[3] else min(lst) if lst[3] < lst[4] else lst[4]
    if len(lst) == 7:
        return min(lst) if lst[0] < lst[1] else min(lst) if lst[1] < lst[2] else min(lst) if lst[2] < lst[3] else min(lst) if lst[3] < lst[4] else min(lst) if lst[4] < lst[5] else lst[5]
    if len(lst) == 8:
        return min(lst) if lst[0] < lst[1] else min(lst) if lst[1] < lst[2] else min(lst) if lst[2] < lst[3] else min(lst) if lst[3] < lst[4] else min(lst) if lst[4] < lst[5] else min(lst) if lst[5] < lst[6] else lst[6]
    if len(lst) == 9:
        return min(lst) if lst[0] < lst[1] else min(lst) if lst[1] < lst[2] else min(lst) if lst[2] < lst[3] else min(lst)