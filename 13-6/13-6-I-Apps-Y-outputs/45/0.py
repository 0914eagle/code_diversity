
def get_min_moves(n):
    # Initialize the minimum number of moves to -1
    min_moves = -1
    
    # Loop through each digit in the number
    for i in range(len(n)):
        # Check if the current digit is 0
        if n[i] == "0":
            # If the current digit is 0, return -1
            return -1
    
    # If the number does not contain any leading zeroes, set the minimum number of moves to 0
    min_moves = 0
    
    # Loop through each digit in the number
    for i in range(len(n)):
        # Check if the current digit is not the last digit in the number
        if i != len(n) - 1:
            # If the current digit is not the last digit, check if the next digit is 0
            if n[i + 1] == "0":
                # If the next digit is 0, increment the minimum number of moves
                min_moves += 1
    
    # Return the minimum number of moves
    return min_moves

def main():
    # Read a single integer n from stdin
    n = int(input().strip())
    
    # Call the get_min_moves function and store the result in min_moves
    min_moves = get_min_moves(n)
    
    # Print the minimum number of moves
    print(min_moves)

if __name__ == '__main__':
    main()

