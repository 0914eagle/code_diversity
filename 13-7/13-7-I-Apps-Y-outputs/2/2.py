
def get_min_moves(n):
    # Initialize the minimum number of moves as -1
    min_moves = -1
    
    # Loop through each digit in the number
    for i in range(len(n)):
        # Check if the current digit is 0
        if n[i] == '0':
            # If the current digit is 0, continue to the next digit
            continue
        # Check if the current digit is 2 or 5
        if n[i] in ['2', '5']:
            # If the current digit is 2 or 5, return 0 as the minimum number of moves
            return 0
        # Check if the current digit is 1
        if n[i] == '1':
            # If the current digit is 1, swap it with the next digit
            n = n[:i] + n[i+1] + n[i] + n[i+2:]
            # Increment the minimum number of moves
            min_moves += 1
            # Continue to the next digit
            continue
        # Check if the current digit is 3 or 6
        if n[i] in ['3', '6']:
            # If the current digit is 3 or 6, swap it with the previous digit
            n = n[:i-1] + n[i-1] + n[i] + n[i+1:]
            # Increment the minimum number of moves
            min_moves += 1
            # Continue to the next digit
            continue
        # Check if the current digit is 4
        if n[i] == '4':
            # If the current digit is 4, swap it with the previous two digits
            n = n[:i-2] + n[i-2] + n[i-1] + n[i] + n[i+1:]
            # Increment the minimum number of moves
            min_moves += 2
            # Continue to the next digit
            continue
        # Check if the current digit is 7 or 9
        if n[i] in ['7', '9']:
            # If the current digit is 7 or 9, swap it with the next two digits
            n = n[:i] + n[i+1] + n[i] + n[i+2] + n[i+3:]
            # Increment the minimum number of moves
            min_moves += 2
            # Continue to the next digit
            continue
    
    # If the minimum number of moves is still -1, return -1
    if min_moves == -1:
        return -1
    # Otherwise, return the minimum number of moves
    return min_moves

def main():
    # Read a single integer n from stdin
    n = int(input())
    
    # Call the get_min_moves function and print the result
    print(get_min_moves(n))

if __name__ == '__main__':
    main()

