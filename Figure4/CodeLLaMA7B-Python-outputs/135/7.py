def can_arrange(arr):
    
    # Find the largest element in the array.
    largest = max(arr)

    # Create a new array of the same length as the original array.
    new_arr = [None] * len(arr)

    # Iterate through the original array.
    for i in range(len(arr)):
        # If the current element is less than or equal to the largest element
        # then set the new array's element at the current index to the
        # difference between the current element and the largest element.
        if arr[i] <= largest:
            new_arr[i] = largest - arr[i]
        # Otherwise set the new array's element at the current index to -1.
        else:
            new_arr[i] = -1

    # Iterate through the new array.
    for i in range(len(new_arr)):
        # If the current element is not equal to the largest element then
        # return the current index.
        if new_arr[i] != largest:
            return i

    # If the function has reached this point then return -1.
    return -1


print(can_arrange([1, 2, 4, 3, 5]))
print(can_arrange([1, 2, 3]))
