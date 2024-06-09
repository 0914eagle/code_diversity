
def solve(a):
    # Initialize the sum of non-deleted elements
    sum_non_deleted = 0
    # Initialize the number of moves
    num_moves = 0
    # Initialize the parity of the last deleted element
    last_parity = None
    # Sort the array in non-decreasing order
    a.sort()
    # Loop through the array
    for i in range(len(a)):
        # If it is the first move, choose any element and delete it
        if num_moves == 0:
            sum_non_deleted += a[i]
            last_parity = a[i] % 2
            num_moves += 1
        # If it is the second or any next move
        else:
            # If the last deleted element was odd
            if last_parity == 1:
                # Choose any even element and delete it
                if a[i] % 2 == 0:
                    sum_non_deleted += a[i]
                    last_parity = a[i] % 2
                    num_moves += 1
            # If the last deleted element was even
            else:
                # Choose any odd element and delete it
                if a[i] % 2 == 1:
                    sum_non_deleted += a[i]
                    last_parity = a[i] % 2
                    num_moves += 1
        # If after some move Polycarp cannot make a move, the game ends
        if num_moves == len(a):
            break
    # Return the minimum possible sum of non-deleted elements
    return sum_non_deleted

