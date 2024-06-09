
def get_number_of_first_moves(numbers):
    # Initialize a set to store the numbers that have been taken
    taken_numbers = set()
    # Initialize a list to store the first moves
    first_moves = []
    # Iterate through the numbers
    for number in numbers:
        # Check if the number has not been taken yet
        if number not in taken_numbers:
            # Add the number to the taken numbers set
            taken_numbers.add(number)
            # Add the number to the first moves list
            first_moves.append(number)
    # Return the length of the first moves list
    return len(first_moves)

def get_winnable_first_moves(numbers):
    # Initialize a set to store the numbers that have been taken
    taken_numbers = set()
    # Initialize a list to store the first moves
    first_moves = []
    # Iterate through the numbers
    for number in numbers:
        # Check if the number has not been taken yet
        if number not in taken_numbers:
            # Add the number to the taken numbers set
            taken_numbers.add(number)
            # Add the number to the first moves list
            first_moves.append(number)
    # Return the length of the first moves list
    return len(first_moves)

if __name__ == '__main__':
    num_numbers = int(input())
    numbers = [int(x) for x in input().split()]
    print(get_number_of_first_moves(numbers))
    print(get_winnable_first_moves(numbers))

