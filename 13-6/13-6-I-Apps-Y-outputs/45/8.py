
def get_min_moves(n):
    # Initialize the minimum number of moves to -1
    min_moves = -1
    
    # Loop through each digit in the number
    for i in range(len(n)):
        # Check if the digit is 0
        if n[i] == "0":
            # If it is, continue to the next digit
            continue
        # Check if the digit is 5
        elif n[i] == "5":
            # If it is, return 0 since we can obtain a number divisible by 25 immediately
            return 0
        # Otherwise, swap the digit with the next digit
        else:
            # Swap the digit with the next digit
            n = n[:i] + n[i+1] + n[i] + n[i+2:]
            # Recursively call the function with the new number
            min_moves = get_min_moves(n)
            # If the minimum number of moves is not -1, break the loop
            if min_moves != -1:
                break
    
    # Return the minimum number of moves
    return min_moves

def main():
    # Read a single integer n from stdin
    n = int(input())
    # Call the get_min_moves function and print the result
    print(get_min_moves(n))

if __name__ == '__main__':
    main()

