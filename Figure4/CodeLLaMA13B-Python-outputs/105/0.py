def by_length(arr):
    
    if len(arr) == 0:
        return []
    arr.sort()
    arr.reverse()
    result = []
    for i in arr:
        if i >= 1 and i <= 9:
            result.append(str(i))
    return result


