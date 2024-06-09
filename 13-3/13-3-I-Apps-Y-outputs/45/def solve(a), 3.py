
def solve(a):
    # Initialize the sum of non-deleted elements
    sum_non_deleted = 0
    # Initialize the number of moves
    num_moves = 0
    # Initialize the parity of the last deleted element
    last_parity = None
    # Loop through the array
    for i in range(len(a)):
        # If it's the first move, choose any element and delete it
        if num_moves == 0:
            sum_non_deleted += a[i]
            last_parity = a[i] % 2
            num_moves += 1
        # If it's the second or any next move, choose the element with the opposite parity
        else:
            if last_parity == 0:
                sum_non_deleted += a[i]
                last_parity = 1
            elif last_parity == 1:
                sum_non_deleted += a[i]
                last_parity = 0
            num_moves += 1
    # If all elements are deleted, the sum of non-deleted elements is zero
    if num_moves == len(a):
        sum_non_deleted = 0
    return sum_non_deleted

