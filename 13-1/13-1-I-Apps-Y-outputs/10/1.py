
def get_min_moves(n):
    # Initialize the minimum number of moves to -1
    min_moves = -1
    
    # Loop through each possible move
    for i in range(len(n) - 1):
        # Get the current digit
        curr_digit = n[i]
        
        # Get the next digit
        next_digit = n[i + 1]
        
        # Check if the current digit is 0
        if curr_digit == "0":
            # If the current digit is 0, skip this move
            continue
        
        # Check if the next digit is 0
        if next_digit == "0":
            # If the next digit is 0, skip this move
            continue
        
        # Get the new number after the move
        new_num = n[:i] + next_digit + curr_digit + n[i + 2:]
        
        # Check if the new number is divisible by 25
        if int(new_num) % 25 == 0:
            # If the new number is divisible by 25, return the minimum number of moves
            return i + 1
    
    # If no move results in a number divisible by 25, return -1
    return min_moves

