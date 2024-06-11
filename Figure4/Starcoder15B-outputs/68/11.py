def pluck(arr):
    
    if not arr:
        return []
    smallest_even = None
    smallest_even_index = None
    for i, val in enumerate(arr):
        if val % 2 == 0:
            if smallest_even is None:
                smallest_even = val
                smallest_even_index = i
            elif val < smallest_even:
                smallest_even = val
                smallest_even_index = i
    if smallest_even is None:
        return []
    return [smallest_even, smallest_even_index]


