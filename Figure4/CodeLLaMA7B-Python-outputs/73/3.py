def smallest_change(arr):
    
    # check if array is palindrome
    if arr == arr[::-1]:
        return 0

    # get the length of the array
    n = len(arr)

    # get the middle of the array
    middle = n // 2

    # get the first half of the array
    first_half = arr[:middle]

    # get the second half of the array
    second_half = arr[middle:]

    # reverse the second half of the array
    second_half = second_half[::-1]

    # get the number of changes required to make the array palindrome
    changes = 0

    # loop through the first half of the array
    for i in range(middle):
        # if the first half of the array is not equal to the second half of the array
        if first_half[i] != second_half[i]:
            # increment the number of changes required to make the array palindrome
            changes += 1

    return changes


print(smallest_change([1, 2, 3, 5, 4, 7, 9, 6]))
print(smallest_change([1, 2, 3, 4, 3, 2, 2]))
print(smallest_change([1, 2, 3, 2, 1]))
