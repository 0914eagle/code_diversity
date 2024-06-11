def smallest_change(arr):
    
    # Your code here
    # 1. Find the middle of the array
    # 2. Reverse the second half of the array
    # 3. Compare the two halves
    # 4. If they are equal, return 0
    # 5. If they are not equal, return the number of elements that are different
    # 6. If the array is odd, return the number of elements that are different plus 1
    # 7. If the array is even, return the number of elements that are different plus 2
    # 8. If the array is empty, return 0

    if len(arr) == 0:
        return 0

    middle = len(arr) // 2
    arr_copy = arr.copy()
    arr_copy[middle:] = arr_copy[middle:][::-1]

    if arr == arr_copy:
        return 0

    count = 0
    for i in range(len(arr)):
        if arr[i] != arr_copy[i]:
            count += 1

    if len(arr) % 2 == 0:
        return count
    else:
        return count + 1


print(smallest_change([1, 2, 3, 5, 4, 7, 9, 6]))
print(smallest_change([1, 2, 3, 4, 3, 2, 2]))
print(smallest_change([1, 2, 3, 2, 1]))
print(smallest_change([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(smallest_change([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))
print(smallest_change([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))
print(smallest_change([1, 2, 3, 4, 5,