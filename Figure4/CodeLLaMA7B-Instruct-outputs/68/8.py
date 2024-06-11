

def pluck(arr):
    

    # Check if the array is empty or if there are no even values
    if not arr or not any(n % 2 == 0 for n in arr):
        return []

    # Find the smallest even value and its index
    smallest_even_value = min(n for n in arr if n % 2 == 0)
    smallest_even_index = arr.index(smallest_even_value)

    # Return the plucked node in a list
    return [smallest_even_value, smallest_even_index]

# Test cases
print(pluck([4, 2, 3]))  # [2, 1]
print
