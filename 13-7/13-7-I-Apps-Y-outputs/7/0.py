
def polycarp(arr):
    # Initialize the sum of non-deleted elements
    sum_non_deleted = sum(arr)
    # Initialize the number of moves
    num_moves = 0
    # Loop until the array is empty
    while arr:
        # If it is the first move, choose any element and delete it
        if num_moves == 0:
            del arr[0]
        # If it is the second or any next move:
        else:
            # If the last deleted element was odd, choose any even element and delete it
            if arr[num_moves - 1] % 2 == 1:
                for i in range(len(arr)):
                    if arr[i] % 2 == 0:
                        del arr[i]
                        break
            # If the last deleted element was even, choose any odd element and delete it
            else:
                for i in range(len(arr)):
                    if arr[i] % 2 == 1:
                        del arr[i]
                        break
        # Increment the number of moves
        num_moves += 1
    # Return the minimum possible sum of non-deleted elements
    return sum_non_deleted

