def can_arrange(arr):
    
    # TODO: Write your solution here
    # O(n) time | O(n) space
    # if len(arr) < 2:
    #     return -1
    #
    # max_val = max(arr)
    # min_val = min(arr)
    #
    # if max_val - min_val + 1 != len(arr):
    #     return -1
    #
    # index_map = {}
    # for i in range(len(arr)):
    #     index_map[arr[i]] = i
    #
    # for i in range(len(arr)):
    #     if arr[i] - 1 not in index_map:
    #         return i
    #     else:
    #         return -1

    # O(n) time | O(1) space
    if len(arr) < 2:
        return -1

    max_val = max(arr)
    min_val = min(arr)

    if max_val - min_val + 1 != len(arr):
        return -1

    for i in range(len(arr)):
        if arr[i] - 1 not in arr:
            return i
    return -1


print(can_arrange([1, 2, 4, 3, 5]))
print(can_arrange([1, 2, 3]))
