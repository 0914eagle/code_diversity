def can_arrange(arr):
    
    # O(n) time | O(1) space
    # if len(arr) == 1:
    #     return -1
    #
    # # find the largest index of an element which is not greater than or equal
    # # to the element immediately preceding it
    # max_index = 0
    # for i in range(1, len(arr)):
    #     if arr[i] <= arr[i - 1]:
    #         max_index = i
    #
    # # if no such element exists then return -1
    # if max_index == 0:
    #     return -1
    #
    # # find the index of the element which is not greater than or equal to the
    # # element immediately preceding it
    # for i in range(max_index, -1, -1):
    #     if arr[i] > arr[i - 1]:
    #         return i
    #
    # return -1

    # O(n) time | O(1) space
    # if len(arr) == 1:
    #     return -1
    #
    # # find the largest index of an element which is not greater than or equal
    # # to the element immediately preceding it
    # max_index = 0
    # for i in range(1, len(arr)):
    #     if arr[i] <= arr[i - 1]:
    #         max_index = i
    #
    # # if no such element exists then return -1
    # if max_index == 0:
    #     return -1
    #
    # # find the index of the element which is not greater than or equal to the
    # # element immediately preceding it
    # for i in range(max_index, -1, -1):
    #     if arr[i] > arr[i - 1]:
    #         return i
    #
    # return -1

    # O(n) time | O(1) space
    if len(arr) == 1:
        return -1

    # find the largest index of an element which is not greater than or equal
    # to the element immediately preceding