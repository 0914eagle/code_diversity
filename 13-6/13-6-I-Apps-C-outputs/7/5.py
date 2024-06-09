
import sys

def solve(n, a):
    # Initialize the number of piles to 0
    num_piles = 0
    # Initialize the maximum number of boxes in a pile to 0
    max_boxes = 0
    # Iterate over the boxes
    for i in range(n):
        # Initialize the number of boxes in the current pile to 0
        num_boxes = 0
        # Iterate over the remaining boxes
        for j in range(i, n):
            # If the current box is divisible by the ith box
            if a[j] % a[i] == 0:
                # Increment the number of boxes in the current pile
                num_boxes += 1
                # Remove the current box from the list
                a.pop(j)
                # Break out of the inner loop
                break
        # If the current pile has more boxes than the maximum number of boxes in a pile
        if num_boxes > max_boxes:
            # Increment the number of piles
            num_piles += 1
            # Update the maximum number of boxes in a pile
            max_boxes = num_boxes
    # Return the number of piles
    return num_piles

n = int(input())
a = list(map(int, input().split()))
print(solve(n, a))

