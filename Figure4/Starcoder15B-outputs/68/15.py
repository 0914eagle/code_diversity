def pluck(arr):
    
    smallest_even_value = None
    smallest_even_value_index = None
    for index, value in enumerate(arr):
        if value % 2 == 0:
            if smallest_even_value is None:
                smallest_even_value = value
                smallest_even_value_index = index
            elif value < smallest_even_value:
                smallest_even_value = value
                smallest_even_value_index = index
    return [smallest_even_value, smallest_even_value_index] if smallest_even_value is not None else []


