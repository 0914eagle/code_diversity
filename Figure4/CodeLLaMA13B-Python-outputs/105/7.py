def by_length(arr):
    
    if len(arr) == 0:
        return []
    arr.sort()
    arr.reverse()
    return [str(i) if i < 0 or i > 9 else str(i) + " " + str(i) for i in arr]


