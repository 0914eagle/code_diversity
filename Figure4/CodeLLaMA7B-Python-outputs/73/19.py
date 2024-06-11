def smallest_change(arr):
    
    # Your code here
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return 0
    if len(arr) == 2:
        if arr[0] == arr[1]:
            return 0
        else:
            return 1
    if len(arr) == 3:
        if arr[0] == arr[2]:
            return 1
        else:
            return 2
    if len(arr) % 2 == 0:
        return smallest_change(arr[:len(arr) // 2]) + smallest_change(arr[len(arr) // 2:])
    else:
        return smallest_change(arr[:len(arr) // 2]) + smallest_change(arr[len(arr) // 2 + 1:])


print(smallest_change([1, 2, 3, 5, 4, 7, 9, 6]))
print(smallest_change([1, 2, 3, 4, 3, 2, 2]))
print(smallest_change([1, 2, 3, 2, 1]))
print(smallest_change([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(smallest_change([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))
print(smallest_change([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))
print(smallest_change([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]))
print(smallest_change([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]))