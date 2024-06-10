
def get_input():
    N = int(input())
    numbers = list(map(int, input().split()))
    return N, numbers

def get_number_of_moves(N, numbers):
    # Initialize a set to store the numbers that have been taken
    taken_numbers = set()
    
    # Initialize a variable to store the number of moves
    number_of_moves = 0
    
    # Iterate through the numbers
    for number in numbers:
        # If the number has not been taken, add it to the set of taken numbers
        if number not in taken_numbers:
            taken_numbers.add(number)
            number_of_moves += 1
    
    # Return the number of moves
    return number_of_moves

def get_possible_first_moves(N, numbers):
    # Initialize a list to store the possible first moves
    possible_first_moves = []
    
    # Iterate through the numbers
    for number in numbers:
        # If the number has not been taken, add it to the list of possible first moves
        if number not in possible_first_moves:
            possible_first_moves.append(number)
    
    # Return the list of possible first moves
    return possible_first_moves

def get_number_of_possible_first_moves(N, numbers):
    # Get the list of possible first moves
    possible_first_moves = get_possible_first_moves(N, numbers)
    
    # Return the length of the list of possible first moves
    return len(possible_first_moves)

def main():
    # Get the input
    N, numbers = get_input()
    
    # Get the number of possible first moves
    number_of_possible_first_moves = get_number_of_possible_first_moves(N, numbers)
    
    # Print the number of possible first moves
    print(number_of_possible_first_moves)

if __name__ == '__main__':
    main()

