
def get_number_of_moves(numbers):
    # Initialize a set to store the numbers that have been taken
    taken_numbers = set()
    # Initialize a list to store the moves
    moves = []
    # Iterate through the numbers
    for number in numbers:
        # If the number has not been taken, add it to the set of taken numbers and add the move to the list of moves
        if number not in taken_numbers:
            taken_numbers.add(number)
            moves.append(number)
        # If the number has been taken, find the adjacent numbers and add them to the set of taken numbers and the list of moves
        else:
            adjacent_numbers = [numbers[i-1] for i in range(1, len(numbers)) if numbers[i-1] != number and numbers[i-1] not in taken_numbers]
            for adjacent_number in adjacent_numbers:
                taken_numbers.add(adjacent_number)
                moves.append(adjacent_number)
    # Return the length of the list of moves
    return len(moves)

def get_first_moves(numbers):
    # Initialize a list to store the first moves
    first_moves = []
    # Iterate through the numbers
    for number in numbers:
        # If the number has not been taken, add it to the list of first moves
        if number not in first_moves:
            first_moves.append(number)
    # Return the list of first moves
    return first_moves

if __name__ == '__main__':
    # Get the number of numbers from the user
    n = int(input())
    # Get the numbers from the user
    numbers = [int(x) for x in input().split()]
    # Get the number of moves
    moves = get_number_of_moves(numbers)
    # Get the first moves
    first_moves = get_first_moves(numbers)
    # Print the number of first moves
    print(len(first_moves))

