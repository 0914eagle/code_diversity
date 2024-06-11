

def pluck(arr):
    

    # Find the smallest even value in the array
    smallest_even_value = float('inf')
    smallest_index = -1
    for i, value in enumerate(arr):
        if value % 2 == 0 and value < smallest_even_value:
            smallest_even_value = value
            smallest_index = i

    # If there are no even values or the array is empty, return []
    if smallest_index == -1:
        return []

    # Return the plucked node in a list, [ smalest_value, its index ]
    return [smallest_even_value, smallest_index]

# Test cases:
