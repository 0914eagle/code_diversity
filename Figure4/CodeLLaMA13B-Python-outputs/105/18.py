def by_length(arr):
    
    if len(arr) == 0:
        return []

    arr.sort()
    arr.reverse()
    result = []
    for num in arr:
        if num >= 1 and num <= 9:
            result.append(str(num))
        else:
            result.append(str(num))
    return result


