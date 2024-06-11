

def next_smallest(lst):
    
    if len(lst) < 2:
        return None
    sorted_lst = sorted(lst)
    for i in range(len(lst)):
        if sorted_lst[i] != lst[i]:
            return sorted_lst[i+1]
    return None


