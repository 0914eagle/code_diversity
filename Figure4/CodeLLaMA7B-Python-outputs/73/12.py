def smallest_change(arr):
    
    # TODO: Write your solution here
    # if len(arr) < 2:
    #     return 0
    # if len(arr) == 2:
    #     if arr[0] == arr[1]:
    #         return 0
    #     else:
    #         return 1
    #
    # if arr[0] == arr[-1]:
    #     return smallest_change(arr[1:-1])
    # else:
    #     return 1 + smallest_change(arr[1:-1])

    # if len(arr) < 2:
    #     return 0
    # if len(arr) == 2:
    #     if arr[0] == arr[1]:
    #         return 0
    #     else:
    #         return 1
    #
    # if arr[0] == arr[-1]:
    #     return smallest_change(arr[1:-1])
    # else:
    #     return 1 + smallest_change(arr[1:-1])

    if len(arr) < 2:
        return 0
    if len(arr) == 2:
        if arr[0] == arr[1]:
            return 0
        else:
            return 1

    if arr[0] == arr[-1]:
        return smallest_change(arr[1:-1])
    else:
        return 1 + smallest_change(arr[1:-1])


print(smallest_change([1, 2, 3, 5, 4, 7, 9, 6]))
print(smallest_change([1, 2, 3, 4, 3, 2, 2]))
print(smallest_change([1, 2, 3, 2, 1]))
print(smallest_change([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(smallest_change([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))
