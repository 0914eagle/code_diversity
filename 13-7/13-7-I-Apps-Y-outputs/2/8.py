
def get_min_moves(n):
    # Initialize the minimum number of moves to -1
    min_moves = -1
    
    # Loop through each digit in the number
    for i in range(len(n)):
        # Get the current digit
        curr_digit = n[i]
        
        # Check if the current digit is 0
        if curr_digit == "0":
            # If the current digit is 0, continue to the next digit
            continue
        
        # Get the previous digit
        prev_digit = n[i-1] if i > 0 else "0"
        
        # Get the next digit
        next_digit = n[i+1] if i < len(n)-1 else "0"
        
        # Check if the previous digit is not 0 and the next digit is 0
        if prev_digit != "0" and next_digit == "0":
            # If the previous digit is not 0 and the next digit is 0, swap the current digit with the previous digit
            n = n[:i-1] + curr_digit + prev_digit + n[i+1:]
            min_moves = 1
        # Check if the previous digit is 0 and the next digit is not 0
        elif prev_digit == "0" and next_digit != "0":
            # If the previous digit is 0 and the next digit is not 0, swap the current digit with the next digit
            n = n[:i] + next_digit + curr_digit + n[i+2:]
            min_moves = 1
    
    # Return the minimum number of moves
    return min_moves

def main():
    # Read a single integer from stdin and save it in the variable n
    n = input().strip()
    
    # Call the get_min_moves function and save the result in the variable min_moves
    min_moves = get_min_moves(n)
    
    # Print the minimum number of moves
    print(min_moves)

if __name__ == '__main__':
    main()

