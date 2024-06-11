def by_length(arr):
    
    if len(arr) == 0:
        return []
    arr.sort()
    arr.reverse()
    result = []
    for num in arr:
        if num > 0 and num < 10:
            result.append(str(num))
        else:
            result.append('')
    return result


