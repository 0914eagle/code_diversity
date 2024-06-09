
import sys

def solve(R, W, d):
    # Base case: if there are no red or white wine boxes, there is only one way to arrange them
    if R == 0 and W == 0:
        return 1
    
    # Base case: if there is only one red or white wine box, it can only be arranged in one way
    if R == 1 and W == 0:
        return 1
    if R == 0 and W == 1:
        return 1
    
    # Recursive case: arrange the red and white wine boxes recursively
    total = 0
    for i in range(1, min(d+1, R+1)):
        total += solve(R-i, W, d)
    for i in range(1, W+1):
        total += solve(R, W-i, d)
    
    return total % (10**9 + 7)

