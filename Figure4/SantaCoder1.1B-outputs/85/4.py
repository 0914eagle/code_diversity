def add(lst):
    
    if len(lst) == 0:
        return lst
    else:
        return [lst[i] + lst[i+1] for i in range(0, len(lst), 2)]


