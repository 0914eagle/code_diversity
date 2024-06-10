
def get_min_moves(n):
    # Initialize the minimum number of moves to -1
    min_moves = -1
    
    # Loop through each digit in the number
    for i in range(len(n)):
        # Check if the current digit is 0
        if n[i] == '0':
            # If it is, continue to the next digit
            continue
        # Check if the current digit is 5
        elif n[i] == '5':
            # If it is, return 0 as the minimum number of moves
            return 0
        # Check if the current digit is even
        elif int(n[i]) % 2 == 0:
            # If it is, return 1 as the minimum number of moves
            return 1
        # Check if the current digit is odd
        else:
            # If it is, return 2 as the minimum number of moves
            return 2
    
    # If the number does not contain any 0s, 5s, or odd digits, return -1
    return min_moves

def main():
    n = input("Enter a number: ")
    print(get_min_moves(n))

if __name__ == '__main__':
    main()

