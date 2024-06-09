
def solve(n, a):
    # Initialize the number of piles to 0
    piles = 0
    # Loop through each box
    for i in range(n):
        # If the box is not already used
        if a[i] > 0:
            # Initialize the current pile to be the box
            current_pile = [a[i]]
            # Loop through the remaining boxes
            for j in range(i+1, n):
                # If the current box is divisible by the current pile
                if a[j] % current_pile[-1] == 0:
                    # Add the current box to the pile
                    current_pile.append(a[j])
                    # Set the current box to 0 so it cannot be used again
                    a[j] = 0
            # Add the current pile to the total number of piles
            piles += 1
    # Return the total number of piles
    return piles

