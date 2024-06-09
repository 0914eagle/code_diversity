
def get_min_moves(n):
    # Initialize the minimum number of moves to -1
    min_moves = -1
    
    # Loop through each possible move
    for i in range(len(n) - 1):
        # Get the current digit and the next digit
        cur_digit = int(n[i])
        next_digit = int(n[i + 1])
        
        # Check if the current digit is a 0
        if cur_digit == 0:
            # If the current digit is a 0, skip this move
            continue
        
        # Check if the next digit is a 0
        if next_digit == 0:
            # If the next digit is a 0, skip this move
            continue
        
        # Check if the current digit is divisible by 5
        if cur_digit % 5 == 0:
            # If the current digit is divisible by 5, skip this move
            continue
        
        # Check if the next digit is divisible by 5
        if next_digit % 5 == 0:
            # If the next digit is divisible by 5, skip this move
            continue
        
        # If the current digit is not divisible by 5 and the next digit is not divisible by 5,
        # update the minimum number of moves
        min_moves = min(min_moves, 1)
    
    # Return the minimum number of moves
    return min_moves

def get_min_moves_2(n):
    # Initialize the minimum number of moves to -1
    min_moves = -1
    
    # Loop through each possible move
    for i in range(len(n) - 1):
        # Get the current digit and the next digit
        cur_digit = int(n[i])
        next_digit = int(n[i + 1])
        
        # Check if the current digit is a 0
        if cur_digit == 0:
            # If the current digit is a 0, skip this move
            continue
        
        # Check if the next digit is a 0
        if next_digit == 0:
            # If the next digit is a 0, skip this move
            continue
        
        # Check if the current digit is divisible by 5
        if cur_digit % 5 == 0:
            # If the current digit is divisible by 5, skip this move
            continue
        
        # Check if the next digit is divisible by 5
        if next_digit % 5 == 0:
            # If the next digit is divisible by 5, skip this move
            continue
        
        # If the current digit is not divisible by 5 and the next digit is not divisible by 5,
        # update the minimum number of moves
        min_moves = min(min_moves, 1)
    
    # Return the minimum number of moves
    return min_moves

if __name__ == '__main__':
    n = int(input())
    print(get_min_moves(n))

