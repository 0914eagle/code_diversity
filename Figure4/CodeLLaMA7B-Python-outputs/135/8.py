def can_arrange(arr):
    
    # O(n) time | O(n) space
    # where n is the length of the input array
    # n = len(arr)
    # if n < 2:
    #     return -1
    #
    # max_value = max(arr)
    #
    # # create a new array of the same length as the input array
    # indices = [None] * n
    #
    # # fill the array with the largest index of an element which is not greater
    # # than or equal to the element immediately preceding it
    # for i in range(n - 1, -1, -1):
    #     if arr[i] <= max_value:
    #         max_value = arr[i]
    #     indices[i] = max_value
    #
    # # return the largest index of an element which is not greater than or equal
    # # to the element immediately preceding it
    # return indices.index(max_value)

    # O(n) time | O(1) space
    # where n is the length of the input array
    # n = len(arr)
    # if n < 2:
    #     return -1
    #
    # # create a new array of the same length as the input array
    # indices = [None] * n
    #
    # # fill the array with the largest index of an element which is not greater
    # # than or equal to the element immediately preceding it
    # for i in range(n - 1, -1, -1):
    #     if arr[i] <= arr[indices[i + 1]]:
    #         indices[i] = i + 1
    #     else:
    #         indices[i] = indices[i + 1]
    #
    # # return the largest index of an element which is not greater than or equal
    # # to the element immediately preceding it
    # return indices[0]

    # O(n) time | O(1) space
    # where n is the length of the input array
    # n = len(arr)
    # if n < 2:
    #     return -1
    #