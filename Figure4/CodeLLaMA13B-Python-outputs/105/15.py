def by_length(arr):
    
    if len(arr) == 0:
        return []
    else:
        arr.sort()
        arr.reverse()
        result = []
        for i in arr:
            if i > 0 and i < 10:
                result.append(str(i))
            else:
                result.append('')
        return result


