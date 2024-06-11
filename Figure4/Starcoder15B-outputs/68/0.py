def pluck(arr):
    
    if not arr:
        return []
    min_even_value = float('inf')
    min_even_index = -1
    for i, value in enumerate(arr):
        if value % 2 == 0 and value < min_even_value:
            min_even_value = value
            min_even_index = i
    return [min_even_value, min_even_index]


