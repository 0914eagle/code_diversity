def add(lst):
    
    for i in range(len(lst)):
        if i % 2 == 0:
            lst[i] += lst[i - 1]
    return lst


