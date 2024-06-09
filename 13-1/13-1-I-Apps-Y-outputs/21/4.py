
def solve(a, k):
    n = len(a)
    # Step 1: Sort the array in non-decreasing order
    a.sort()
    # Step 2: Find the minimum and maximum values in the array
    min_val = a[0]
    max_val = a[n-1]
    # Step 3: Initialize the number of moves to 0
    moves = 0
    # Step 4: Loop until we have at least k equal elements in the array
    while True:
        # If the minimum and maximum values are the same, we are done
        if min_val == max_val:
            break
        # If the minimum value is less than the maximum value, we can increase the minimum value by 1
        if min_val < max_val:
            # Find the index of the minimum value and increase it by 1
            min_index = a.index(min_val)
            a[min_index] += 1
            # Increment the number of moves
            moves += 1
        # If the minimum value is greater than the maximum value, we can decrease the maximum value by 1
        else:
            # Find the index of the maximum value and decrease it by 1
            max_index = a.index(max_val)
            a[max_index] -= 1
            # Increment the number of moves
            moves += 1
        # Update the minimum and maximum values after each iteration
        min_val = min(a)
        max_val = max(a)
    return moves

