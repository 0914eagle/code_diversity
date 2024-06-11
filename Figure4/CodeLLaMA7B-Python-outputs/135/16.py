def can_arrange(arr):
    
    # O(n) time | O(1) space
    # if arr is None or len(arr) == 0:
    #     return -1

    # max_value = max(arr)
    # min_value = min(arr)

    # if max_value - min_value + 1 != len(arr):
    #     return -1

    # for i in range(len(arr)):
    #     if arr[i] != i + min_value:
    #         return i - 1

    # return -1

    # O(n) time | O(1) space
    # if arr is None or len(arr) == 0:
    #     return -1

    # max_value = max(arr)
    # min_value = min(arr)

    # if max_value - min_value + 1 != len(arr):
    #     return -1

    # for i in range(len(arr)):
    #     if arr[i] != i + min_value:
    #         return i - 1

    # return -1

    # O(n) time | O(1) space
    if arr is None or len(arr) == 0:
        return -1

    max_value = max(arr)
    min_value = min(arr)

    if max_value - min_value + 1 != len(arr):
        return -1

    for i in range(len(arr)):
        if arr[i] != i + min_value:
            return i - 1

    return -1


print(can_arrange([1, 2, 4, 3, 5]))
print(can_arrange([1, 2, 3]))
