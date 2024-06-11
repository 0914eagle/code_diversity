def smallest_change(arr):
    
    # if the array is already palindromic, return 0
    if arr == arr[::-1]:
        return 0

    # if the array is not palindromic, find the first index where the array is not palindromic
    # and then find the first index where the array is palindromic again
    # return the number of elements between the first non-palindromic index and the first palindromic index
    # if the first non-palindromic index is greater than the first palindromic index, return 0
    for i in range(len(arr)):
        if arr != arr[::-1]:
            for j in range(i, len(arr)):
                if arr == arr[::-1]:
                    return j - i
        else:
            return 0


print(smallest_change([1, 2, 3, 5, 4, 7, 9, 6]))
print(smallest_change([1, 2, 3, 4, 3, 2, 2]))
print(smallest_change([1, 2, 3, 2, 1]))
