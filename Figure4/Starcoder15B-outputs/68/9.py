def pluck(arr):
    
    if not arr:
        return []
    smallest_even = float('inf')
    smallest_even_index = -1
    for i, n in enumerate(arr):
        if n % 2 == 0 and n < smallest_even:
            smallest_even = n
            smallest_even_index = i
    if smallest_even_index == -1:
        return []
    return [smallest_even, smallest_even_index]


if __