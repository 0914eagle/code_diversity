
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
        # If the current element is not equal to the next element, increase the number of moves
        moves += 1
        # If the current element is equal to the minimum element of the array, decrease the number of moves
        if a[i] == min(a):
            moves -= 1
        # If the current element is equal to the maximum element of the array, increase the number of moves
        if a[i] == max(a):
            moves += 1
    # If the number of equal elements is not greater than or equal to k, return -1
    return -1

