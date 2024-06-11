def by_length(arr):
    
    if len(arr) == 0:
        return []
    arr.sort()
    arr.reverse()
    return [str(num) if num < 1 or num > 9 else str(num)[::-1] for num in arr]


