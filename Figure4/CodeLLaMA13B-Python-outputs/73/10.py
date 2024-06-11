def smallest_change(arr):
    
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return 0
    if len(arr) == 2:
        return 1

    # O(n)
    arr_set = set(arr)
    # O(n)
    arr_set_len = len(arr_set)

    # O(n)
    if arr_set_len == 1:
        return 0

    # O(n)
    if arr_set_len == 2:
        return 1

    # O(n)
    if arr_set_len == 3:
        return 2

    # O(n)
    if arr_set_len == 4:
        return 3

    # O(n)
    if arr_set_len == 5:
        return 4

    # O(n)
    if arr_set_len == 6:
        return 5

    # O(n)
    if arr_set_len == 7:
        return 6

    # O(n)
    if arr_set_len == 8:
        return 7

    # O(n)
    if arr_set_len == 9:
        return 8

    # O(n)
    if arr_set_len == 10:
        return 9

    # O(n)
    if arr_set_len == 11:
        return 10

    # O(n)
    if arr_set_len == 12:
        return 11

    # O(n)
    if arr_set_len == 13:
        return 12

    # O(n)
    if arr_set_len == 14:
        return 13

    # O(n)
    if arr_set_len == 15:
        return 14

    # O(n)
    if arr_set_len == 16:
        return 15

    # O(n)
    if arr