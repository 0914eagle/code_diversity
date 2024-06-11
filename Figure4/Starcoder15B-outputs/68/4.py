def pluck(arr):
    
    if not arr:
        return []
    min_even = min(filter(lambda x: x % 2 == 0, arr))
    return [min_even, arr.index(min_even)]


