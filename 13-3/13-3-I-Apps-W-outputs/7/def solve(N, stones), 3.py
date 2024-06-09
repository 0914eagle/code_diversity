
def solve(N, stones):
    # Initialize the number of operations to 0
    operations = 0

    # Loop through the stones from left to right
    for i in range(N):
        # If the current stone is white and the next stone is red, we need to perform an operation
        if stones[i] == "W" and stones[i+1] == "R":
            # Increment the number of operations
            operations += 1

            # If the current stone is the first stone, we can only change its color
            if i == 0:
                # Change the color of the current stone to red
                stones[i] = "R"
            # Otherwise, we can swap the current stone with the previous stone
            else:
                # Swap the current stone with the previous stone
                stones[i], stones[i-1] = stones[i-1], stones[i]

    # Return the number of operations needed
    return operations

