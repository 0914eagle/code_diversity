def pluck(arr):
    
    if not arr:
        return []

    smallest_even = None
    smallest_even_index = None

    for i, n in enumerate(arr):
        if n % 2 == 0:
            if smallest_even is None or n < smallest_even:
                smallest_even = n
                smallest_even_index = i

    if smallest_even is None:
        return []

    return [smallest_even, smallest_even_index]


