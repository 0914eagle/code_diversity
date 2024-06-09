
def get_number_of_moves(numbers):
    # Initialize a set to store the numbers that have been taken
    taken_numbers = set()
    # Initialize a list to store the moves that Ivana can make
    moves = []
    # Loop through the numbers
    for number in numbers:
        # Check if the number has already been taken
        if number not in taken_numbers:
            # Add the number to the set of taken numbers
            taken_numbers.add(number)
            # Check if the number is odd
            if number % 2 == 1:
                # Add the number to the list of moves
                moves.append(number)
    # Return the length of the list of moves
    return len(moves)

def main():
    # Read the number of numbers and the numbers from stdin
    n = int(input())
    numbers = [int(x) for x in input().split()]
    # Call the function to get the number of moves that Ivana can make
    moves = get_number_of_moves(numbers)
    # Print the number of moves
    print(moves)

if __name__ == '__main__':
    main()

