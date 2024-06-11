def pluck(arr):
    
    if not arr:
        return []
    smallest_even = None
    smallest_even_index = None
    for i, v in enumerate(arr):
        if v % 2 == 0:
            if smallest_even is None or v < smallest_even:
                smallest_even = v
                smallest_even_index = i
    return [smallest_even, smallest_even_index]

