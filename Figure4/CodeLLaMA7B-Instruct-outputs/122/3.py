

def add_elements(arr, k):
    
    # Check if the input is valid
    if not arr or k < 1 or k > len(arr):
        return None

    # Initialize a variable to store the sum
    sum = 0

    # Iterate over the first k elements of the array
    for i in range(k):
        # Check if the element has at most two digits
        if len(str(arr[i])) <= 2:
            # Add the element to the sum
            sum += arr[i]

    # Return the sum
    return sum

