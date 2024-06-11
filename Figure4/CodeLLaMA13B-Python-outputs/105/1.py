def by_length(arr):
    
    if len(arr) == 0:
        return []
    elif len(arr) == 1:
        return [str(arr[0])]
    else:
        arr.sort()
        arr.reverse()
        return [str(i) for i in arr if 1 <= i <= 9]


