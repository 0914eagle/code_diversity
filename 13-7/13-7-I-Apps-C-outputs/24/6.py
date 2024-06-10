
def get_first_moves(numbers):
    # Initialize a set to store the first moves
    first_moves = set()
    
    # Iterate over the numbers
    for i in range(len(numbers)):
        # Get the current number
        current_number = numbers[i]
        
        # Get the adjacent numbers
        adjacent_numbers = [numbers[(i - 1) % len(numbers)], numbers[(i + 1) % len(numbers)]]
        
        # Add the current number to the set of first moves if it is not already in the set
        if current_number not in first_moves:
            first_moves.add(current_number)
        
        # Add the adjacent numbers to the set of first moves if they are not already in the set
        for adjacent_number in adjacent_numbers:
            if adjacent_number not in first_moves:
                first_moves.add(adjacent_number)
    
    # Return the set of first moves
    return first_moves

def get_winnable_first_moves(numbers):
    # Initialize a set to store the winnable first moves
    winnable_first_moves = set()
    
    # Iterate over the numbers
    for i in range(len(numbers)):
        # Get the current number
        current_number = numbers[i]
        
        # Get the adjacent numbers
        adjacent_numbers = [numbers[(i - 1) % len(numbers)], numbers[(i + 1) % len(numbers)]]
        
        # Add the current number to the set of winnable first moves if it is not already in the set and if it is odd
        if current_number not in winnable_first_moves and current_number % 2 == 1:
            winnable_first_moves.add(current_number)
        
        # Add the adjacent numbers to the set of winnable first moves if they are not already in the set and if they are odd
        for adjacent_number in adjacent_numbers:
            if adjacent_number not in winnable_first_moves and adjacent_number % 2 == 1:
                winnable_first_moves.add(adjacent_number)
    
    # Return the set of winnable first moves
    return winnable_first_moves

def main():
    # Read the input
    N = int(input())
    numbers = list(map(int, input().split()))
    
    # Get the set of first moves
    first_moves = get_first_moves(numbers)
    
    # Get the set of winnable first moves
    winnable_first_moves = get_winnable_first_moves(numbers)
    
    # Print the number of winnable first moves
    print(len(winnable_first_moves))

if __name__ == '__main__':
    main()

