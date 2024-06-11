def pluck(arr):
    
    if len(arr) == 0:
        return []
    evens = []
    for i, val in enumerate(arr):
        if val % 2 == 0:
            evens.append([val, i])
    if len(evens) == 0:
        return []
    evens.sort()
    return evens[0]


if