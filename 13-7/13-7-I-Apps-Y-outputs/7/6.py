
def solve(a):
    # Initialize the sum of non-deleted elements
    sum_non_deleted = sum(a)
    # Initialize the number of moves
    num_moves = 0
    # Loop until all elements are deleted
    while a:
        # If it is the first move, choose any element and delete it
        if num_moves == 0:
            element = a.pop()
        # If it is the second or any next move, choose any element with the only restriction
        else:
            # If the last deleted element was odd, choose any even element and delete it
            if element % 2 == 1:
                element = a.pop(a.index(next(x for x in a if x % 2 == 0)))
            # If the last deleted element was even, choose any odd element and delete it
            else:
                element = a.pop(a.index(next(x for x in a if x % 2 == 1)))
        # Update the sum of non-deleted elements
        sum_non_deleted -= element
        # Increment the number of moves
        num_moves += 1
    # Return the minimum possible sum of non-deleted elements
    return sum_non_deleted

