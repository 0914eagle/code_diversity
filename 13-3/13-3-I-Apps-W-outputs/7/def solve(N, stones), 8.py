
def solve(N, stones):
    # Initialize the number of operations to 0
    operations = 0

    # Loop through the stones from left to right
    for i in range(N):
        # If the current stone is white and the next stone is red, we need to perform an operation
        if stones[i] == "W" and stones[i+1] == "R":
            # Increment the number of operations
            operations += 1

            # If the current stone is the first stone, we need to swap it with the next stone
            if i == 0:
                # Swap the current stone with the next stone
                stones[i], stones[i+1] = stones[i+1], stones[i]

            # If the current stone is not the first stone, we need to swap it with the previous stone
            else:
                # Swap the current stone with the previous stone
                stones[i], stones[i-1] = stones[i-1], stones[i]

    # Return the number of operations needed
    return operations

