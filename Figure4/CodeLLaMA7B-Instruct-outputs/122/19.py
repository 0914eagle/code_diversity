

def add_elements(arr, k):
    
    # Initialize a variable to store the sum
    sum = 0

    # Iterate over the first k elements of arr
    for i in range(k):
        # If the current element has at most two digits
        if len(str(arr[i])) <= 2:
            # Add the current element to the sum
            sum += arr[i]

    # Return the sum
    return sum

