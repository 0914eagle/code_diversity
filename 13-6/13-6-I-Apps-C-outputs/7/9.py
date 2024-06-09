
def solve(n, a):
    # Initialize the number of piles to 0
    piles = 0
    # Initialize the maximum number of boxes in a pile to 0
    max_boxes = 0
    # Iterate over each box
    for i in range(n):
        # Initialize the number of boxes in the current pile to 0
        current_piles = 0
        # Iterate over each box again
        for j in range(n):
            # Check if the current box is a multiple of the current box
            if a[i] % a[j] == 0:
                # Increment the number of boxes in the current pile
                current_piles += 1
        # Check if the current pile has the maximum number of boxes
        if current_piles > max_boxes:
            # Update the maximum number of boxes
            max_boxes = current_piles
            # Increment the number of piles
            piles += 1
    # Return the number of piles modulo 10^9 + 7
    return piles % 1000000007

