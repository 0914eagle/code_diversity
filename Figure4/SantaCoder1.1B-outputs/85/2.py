def add(lst):
    
    for i in range(0, len(lst), 2):
        lst[i] += lst[i + 1]
    return lst


