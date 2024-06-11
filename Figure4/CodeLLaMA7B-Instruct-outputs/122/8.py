

def add_elements(arr, k):
    
    # Initialize a variable to store the sum
    sum = 0

    # Iterate over the first k elements of arr
    for i in range(k):
        # If the current element is less than or equal to 99, add it to the sum
        if arr[i] <= 99:
            sum += arr[i]

    # Return the sum
    return sum

