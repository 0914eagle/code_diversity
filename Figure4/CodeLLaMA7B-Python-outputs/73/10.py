def smallest_change(arr):
    
    # if the array is already palindromic, return 0
    if arr == arr[::-1]:
        return 0

    # if the array is not palindromic, find the first index of the first
    # non-palindromic element
    first_non_palindromic_index = 0
    for i in range(len(arr) // 2):
        if arr[i] != arr[len(arr) - i - 1]:
            first_non_palindromic_index = i
            break

    # find the last index of the first non-palindromic element
    last_non_palindromic_index = len(arr) - 1
    for i in range(len(arr) // 2 + 1, len(arr)):
        if arr[i] != arr[len(arr) - i - 1]:
            last_non_palindromic_index = i
            break

    # if the first and last non-palindromic elements are the same, return 1
    if arr[first_non_palindromic_index] == arr[last_non_palindromic_index]:
        return 1

    # if the first and last non-palindromic elements are different, return 2
    return 2


