def pluck(arr):
    
    if not arr:
        return []

    smallest_even_value = float('inf')
    smallest_even_value_index = -1

    for i, value in enumerate(arr):
        if value % 2 == 0 and value < smallest_even_value:
            smallest_even_value = value
            smallest_even_value_index = i

    if smallest_even_value_index == -1:
        return []

    return [smallest_even_value, smallest_even_value_index]


