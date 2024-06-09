
def get_num_moves(numbers):
    # Initialize a set to store the numbers that have been taken
    taken_numbers = set()
    # Initialize a list to store the moves that Ivana can make
    moves = []
    # Loop through the numbers
    for num in numbers:
        # Check if the number is odd
        if num % 2 != 0:
            # If the number is odd, check if it has been taken already
            if num not in taken_numbers:
                # If the number has not been taken, add it to the set of taken numbers and add the move to the list of moves
                taken_numbers.add(num)
                moves.append(num)
    # Return the length of the list of moves
    return len(moves)

def main():
    # Read the input from stdin
    n = int(input())
    numbers = list(map(int, input().split()))
    # Call the function to get the number of moves that Ivana can make
    num_moves = get_num_moves(numbers)
    # Print the number of moves
    print(num_moves)

if __name__ == '__main__':
    main()

