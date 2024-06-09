
def solve(a, k):
    n = len(a)
    # Sort the array in non-decreasing order
    a.sort()
    # Initialize the number of moves to 0
    moves = 0
    # Initialize the number of equal elements to 0
    equal_elements = 0
    # Loop through the array from left to right
    for i in range(n):
        # If the current element is equal to the next element, increase the number of equal elements
        if i < n-1 and a[i] == a[i+1]:
            equal_elements += 1
        # If the number of equal elements is greater than or equal to k, return the number of moves
        if equal_elements >= k:
            return moves
        # If the current element is not equal to the next element, find the minimum element in the array that is greater than the current element
        if i < n-1 and a[i] < a[i+1]:
            min_element = min(a[i+1:])
            # If the minimum element is not the current element, find the index of the minimum element and increase the number of moves
            if min_element != a[i]:
                min_index = a[i+1:].index(min_element) + i + 1
                moves += 1
                # Increase the value of the minimum element by 1
                a[min_index] += 1
        # If the current element is not equal to the previous element, find the maximum element in the array that is less than the current element
        if i > 0 and a[i] > a[i-1]:
            max_element = max(a[:i])
            # If the maximum element is not the current element, find the index of the maximum element and increase the number of moves
            if max_element != a[i]:
                max_index = a[:i].index(max_element)
                moves += 1
                # Decrease the value of the maximum element by 1
                a[max_index] -= 1
    # If the number of equal elements is not greater than or equal to k, return -1
    return -1

