
def get_min_moves(n):
    # Initialize the minimum number of moves to -1
    min_moves = -1
    
    # Loop through each digit in the number
    for i in range(len(n)):
        # Check if the current digit is a 0
        if n[i] == '0':
            # If it is, continue to the next digit
            continue
        # Check if the current digit is a 5
        elif n[i] == '5':
            # If it is, return 0 as the minimum number of moves
            return 0
        # Otherwise, check if the next digit is a 5
        elif i < len(n) - 1 and n[i+1] == '5':
            # If it is, return 1 as the minimum number of moves
            return 1
        # Otherwise, check if the previous digit is a 5
        elif i > 0 and n[i-1] == '5':
            # If it is, return 1 as the minimum number of moves
            return 1
    
    # If we reach this point, it is impossible to obtain a number that is divisible by 25
    return min_moves

