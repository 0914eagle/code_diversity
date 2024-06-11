def next_smallest(lst):
    
    if not lst:
        return None
    if len(lst) == 1:
        return lst[0]
    if len(lst) == 2:
        return min(lst) if lst[0] < lst[1] else lst[1]
    if len(lst) == 3:
        return min(lst) if lst[0] < lst[1] < lst[2] else min(lst) if lst[0] < lst[1] else lst[2]
    if len(lst) == 4:
        return min(lst) if lst[0] < lst[1] < lst[2] < lst[3] else min(lst) if lst[0] < lst[1] < lst[2] else min(lst) if lst[0] < lst[1] < lst[2] else min(lst) if lst[0] < lst[1] < lst[2] else min(lst) if lst[0] < lst[1] < lst[2] else min(lst) if lst[0] < lst[1] < lst[2] else min(lst) if lst[0] < lst[1] < lst[2] else min(lst) if lst[0] < lst[1] < lst[2] else min(lst) if lst[0] < lst[1] < lst[2] else min(lst) if lst[0] < lst[1] < lst[2] else min(lst) if lst[0] < lst[1] < lst[2] else min(lst) if lst[0] < lst[1] < lst[2] else min(lst) if lst[0] < lst[1] < lst[2] else min(lst) if lst[0] < lst[1] < lst[2] else min(lst) if lst[0] < lst[1] < lst[2] else min(lst) if lst[0] < lst[1] < lst[2] else min(lst) if lst[0] < lst[1] < lst[2] else min(lst) if lst[0] < lst[1] < lst[2] else min(lst) if lst[0] < lst[1] < lst[2] else min(lst) if lst[0]