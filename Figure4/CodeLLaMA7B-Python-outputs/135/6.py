def can_arrange(arr):
    
    # Find the largest element in the array
    largest = max(arr)

    # Create a new array of the same size as the original
    new_arr = [0] * len(arr)

    # Iterate over the original array
    for i in range(len(arr)):
        # If the current element is less than or equal to the largest
        if arr[i] <= largest:
            # Find the index of the largest element which is less than the current element
            j = largest - 1
            while j >= arr[i]:
                if new_arr[j] == 0:
                    new_arr[j] = arr[i]
                    break
                j -= 1

    # Iterate over the new array
    for i in range(len(new_arr)):
        # If the current element is not equal to the largest element
        if new_arr[i] != largest:
            # Return the index of the largest element
            return i

    # If the new array is empty then return -1
    return -1


print(can_arrange([1, 2, 4, 3, 5]))
print(can_arrange([1, 2, 3]))
