
def solve(n, a):
    # Initialize the maximum number of boxes in a pile as 0
    max_boxes = 0
    # Initialize the number of distinct piles as 0
    num_piles = 0
    
    # Iterate over all possible combinations of 3 indices
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                # Check if a[i] divides a[j] and a[k]
                if a[i] % a[j] == 0 and a[i] % a[k] == 0:
                    # Increment the number of boxes in the pile
                    boxes = 1
                    # Check if a[i] is a factor of a[j]
                    if a[j] % a[i] == 0:
                        # Increment the number of boxes in the pile
                        boxes += 1
                    # Check if a[i] is a factor of a[k]
                    if a[k] % a[i] == 0:
                        # Increment the number of boxes in the pile
                        boxes += 1
                    # Check if the number of boxes in the pile is greater than the maximum number of boxes in a pile
                    if boxes > max_boxes:
                        # Update the maximum number of boxes in a pile
                        max_boxes = boxes
                        # Reset the number of distinct piles
                        num_piles = 0
                    # Check if the number of boxes in the pile is equal to the maximum number of boxes in a pile
                    elif boxes == max_boxes:
                        # Increment the number of distinct piles
                        num_piles += 1
    
    # Return the number of distinct piles modulo 10^9 + 7
    return num_piles % 1000000007

