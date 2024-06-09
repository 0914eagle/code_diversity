
def get_min_moves(n):
    # Initialize the minimum number of moves to -1
    min_moves = -1
    
    # Loop through each digit in the number
    for i in range(len(n)):
        # Check if the current digit is a 0
        if n[i] == '0':
            # If it is, continue to the next digit
            continue
        # If the current digit is not a 0, check if the next digit is a 0
        if i < len(n) - 1 and n[i+1] == '0':
            # If it is, swap the current digit with the next digit
            n = n[:i] + n[i+1] + n[i] + n[i+2:]
            # Increment the minimum number of moves
            min_moves += 1
    
    # Return the minimum number of moves
    return min_moves

