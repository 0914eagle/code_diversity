
def get_min_moves(n):
    # Initialize the minimum number of moves to -1
    min_moves = -1
    
    # Loop through each digit in the number
    for i in range(len(n)):
        # Check if the current digit is a 0
        if n[i] == "0":
            # If it is a 0, continue to the next digit
            continue
        # Check if the current digit is a 5
        elif n[i] == "5":
            # If it is a 5, set the minimum number of moves to 0
            min_moves = 0
            break
        # Otherwise, check if the current digit is a multiple of 5
        elif int(n[i]) % 5 == 0:
            # If it is a multiple of 5, set the minimum number of moves to 1
            min_moves = 1
            break
    
    # If the minimum number of moves is still -1, it is impossible to obtain a number that is divisible by 25
    if min_moves == -1:
        return -1
    
    # Loop through each digit in the number
    for i in range(len(n)):
        # Check if the current digit is a 0
        if n[i] == "0":
            # If it is a 0, continue to the next digit
            continue
        # Check if the current digit is a 5
        elif n[i] == "5":
            # If it is a 5, add 1 to the minimum number of moves
            min_moves += 1
        # Otherwise, check if the current digit is a multiple of 5
        elif int(n[i]) % 5 == 0:
            # If it is a multiple of 5, add 1 to the minimum number of moves
            min_moves += 1
    
    # Return the minimum number of moves
    return min_moves

def main():
    # Read a single integer n from stdin
    n = input()
    
    # Call the get_min_moves function and store the result in min_moves
    min_moves = get_min_moves(n)
    
    # Print the minimum number of moves
    print(min_moves)

if __name__ == '__main__':
    main()

