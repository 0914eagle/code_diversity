
def get_min_moves(n):
    # Initialize the minimum number of moves to -1
    min_moves = -1
    
    # Loop through all possible moves
    for i in range(len(n) - 1):
        # Get the current digit
        curr_digit = n[i]
        
        # Get the next digit
        next_digit = n[i + 1]
        
        # Check if the current digit is a 0
        if curr_digit == "0":
            # If the current digit is a 0, skip this move
            continue
        
        # Check if the next digit is a 0
        if next_digit == "0":
            # If the next digit is a 0, skip this move
            continue
        
        # Check if the current digit is a 5
        if curr_digit == "5":
            # If the current digit is a 5, check if the next digit is a 2 or 5
            if next_digit == "2" or next_digit == "5":
                # If the next digit is a 2 or 5, increment the minimum number of moves
                min_moves += 1
        
        # Check if the next digit is a 5
        if next_digit == "5":
            # If the next digit is a 5, check if the current digit is a 2 or 5
            if curr_digit == "2" or curr_digit == "5":
                # If the current digit is a 2 or 5, increment the minimum number of moves
                min_moves += 1
    
    # Return the minimum number of moves
    return min_moves

def main():
    # Read a single integer n from stdin
    n = int(input())
    
    # Call the get_min_moves function and store the result in min_moves
    min_moves = get_min_moves(n)
    
    # Print the minimum number of moves
    print(min_moves)

if __name__ == '__main__':
    main()

