
def solve(a):
    # Sort the array in non-decreasing order
    a.sort()
    # Initialize the sum of non-deleted elements
    sum_non_deleted = 0
    # Initialize the number of moves
    num_moves = 0
    # Loop through the array
    for i in range(len(a)):
        # If it is an even move, choose an even element
        if num_moves % 2 == 0:
            # If the current element is even, choose it
            if a[i] % 2 == 0:
                sum_non_deleted += a[i]
                a.pop(i)
                break
        # If it is an odd move, choose an odd element
        else:
            # If the current element is odd, choose it
            if a[i] % 2 == 1:
                sum_non_deleted += a[i]
                a.pop(i)
                break
        # Increment the number of moves
        num_moves += 1
    # If all elements have been deleted, return the sum of non-deleted elements
    if not a:
        return sum_non_deleted
    # If there are still elements left, return -1
    return -1

