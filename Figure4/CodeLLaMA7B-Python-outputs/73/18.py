def smallest_change(arr):
    
    # TODO: Write your solution here
    # if arr is empty or has one element, return 0
    if len(arr) <= 1:
        return 0

    # if arr is palindrome, return 0
    if arr == arr[::-1]:
        return 0

    # if arr is not palindrome, find the first non-palindrome
    for i in range(len(arr)):
        if arr[i] != arr[len(arr) - i - 1]:
            break

    # if the first non-palindrome is in the middle, return 1
    if i == len(arr) // 2:
        return 1

    # if the first non-palindrome is on the edge, return 2
    if i == 0 or i == len(arr) - 1:
        return 2

    # if the first non-palindrome is not on the edge, return 1
    return 1


# print(smallest_change([1, 2, 3, 5, 4, 7, 9, 6]))
# print(smallest_change([1, 2, 3, 4, 3, 2, 2]))
# print(smallest_change([1, 2, 3, 2, 1]))
