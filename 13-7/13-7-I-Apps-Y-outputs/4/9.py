
def solve(a, b):
    # Find the difference between a and b
    diff = abs(a - b)
    
    # Initialize the minimum number of moves to 0
    min_moves = 0
    
    # While the difference between a and b is greater than 0
    while diff > 0:
        # If the difference is odd, add 1 to make it even
        if diff % 2 == 1:
            diff += 1
        
        # Subtract the minimum number of moves by 1
        min_moves -= 1
        
        # Divide the difference by 2
        diff //= 2
    
    # Return the minimum number of moves
    return min_moves

