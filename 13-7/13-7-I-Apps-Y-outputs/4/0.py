
def get_min_moves(a, b):
    # Initialize the minimum number of moves to infinity
    min_moves = float('inf')
    
    # Loop through all possible values of x and y
    for x in range(1, a+1, 2):
        for y in range(1, a+1, 2):
            # Calculate the new value of a after one move
            new_a = a + x - y
            
            # If the new value of a is equal to b, we have found the minimum number of moves
            if new_a == b:
                return 1
            
            # If the new value of a is less than b, we need to perform more moves
            elif new_a < b:
                # Calculate the number of moves required to get to b from the new value of a
                moves = 1 + get_min_moves(new_a, b)
                
                # Update the minimum number of moves if necessary
                min_moves = min(min_moves, moves)
    
    # Return the minimum number of moves
    return min_moves

