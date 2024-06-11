

def add_elements(arr, k):
    
    # Check if the input is valid
    if not arr or k < 1 or k > len(arr):
        return None

    # Initialize a variable to store the sum
    sum = 0

    # Iterate over the first k elements of the array
    for i in range(k):
        # If the element is less than or equal to 99, add it to the sum
        if arr[i] <= 99:
            sum += arr[i]

    # Return the sum
    return sum

