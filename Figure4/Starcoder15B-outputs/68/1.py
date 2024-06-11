def pluck(arr):
    
    if not arr:
        return []
    even_arr = [i for i in arr if i % 2 == 0]
    if not even_arr:
        return []
    min_even = min(even_arr)
    return [min_even, arr.index(min_even)]


