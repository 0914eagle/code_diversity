
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
            sum_non_deleted -= a[i]
            last_parity = a[i] % 2
            num_moves += 1
        # If it's not the first move, choose an element with the opposite parity
        else:
            if last_parity == 0:
                # If the last deleted element was even, choose an odd element
                if a[i] % 2 == 1:
                    sum_non_deleted -= a[i]
                    last_parity = a[i] % 2
                    num_moves += 1
            else:
                # If the last deleted element was odd, choose an even element
                if a[i] % 2 == 0:
                    sum_non_deleted -= a[i]
                    last_parity = a[i] % 2
                    num_moves += 1
        # If we can't make a move, break the loop
        if num_moves == len(a):
            break
    # Return the minimum possible sum of non-deleted elements
    return sum_non_deleted

