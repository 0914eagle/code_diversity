def pluck(arr):
    
    if not arr:
        return []
    smallest_even_value = min([x for x in arr if x % 2 == 0])
    smallest_even_value_index = arr.index(smallest_even_value)
    return [smallest_even_value, smallest_even_value_index]
