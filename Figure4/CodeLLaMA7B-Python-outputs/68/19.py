def pluck(arr):
    
    # O(n) time | O(1) space
    if not arr:
        return []
    smallest_even_value = None
    smallest_even_index = None
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            if smallest_even_value is None or arr[i] < smallest_even_value:
                smallest_even_value = arr[i]
                smallest_even_index = i
    return [smallest_even_value, smallest_even_index]
