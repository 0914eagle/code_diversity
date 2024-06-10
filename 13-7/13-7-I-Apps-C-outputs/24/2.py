
def get_first_moves(numbers):
    # Initialize a set to store the first moves
    first_moves = set()
    
    # Iterate over the numbers
    for i in range(len(numbers)):
        # Get the current number
        current_number = numbers[i]
        
        # Check if the current number is odd
        if current_number % 2 != 0:
            # Add the current number to the set of first moves
            first_moves.add(current_number)
        
        # Check if the current number is even
        if current_number % 2 == 0:
            # Get the next number
            next_number = numbers[(i + 1) % len(numbers)]
            
            # Check if the next number is odd
            if next_number % 2 != 0:
                # Add the current number to the set of first moves
                first_moves.add(current_number)
    
    # Return the set of first moves
    return first_moves

def get_winnable_first_moves(numbers):
    # Get the set of first moves
    first_moves = get_first_moves(numbers)
    
    # Initialize a set to store the winnable first moves
    winnable_first_moves = set()
    
    # Iterate over the first moves
    for first_move in first_moves:
        # Initialize a set to store the numbers that can be taken
        taken_numbers = set()
        
        # Add the first move to the set of taken numbers
        taken_numbers.add(first_move)
        
        # Iterate over the numbers
        for i in range(len(numbers)):
            # Get the current number
            current_number = numbers[i]
            
            # Check if the current number is adjacent to any of the taken numbers
            if any(abs(current_number - taken_number) == 1 for taken_number in taken_numbers):
                # Add the current number to the set of taken numbers
                taken_numbers.add(current_number)
        
        # Check if the set of taken numbers contains all odd numbers
        if all(number % 2 != 0 for number in taken_numbers):
            # Add the first move to the set of winnable first moves
            winnable_first_moves.add(first_move)
    
    # Return the set of winnable first moves
    return winnable_first_moves

def main():
    # Read the input
    n = int(input())
    numbers = [int(number) for number in input().split()]
    
    # Get the set of winnable first moves
    winnable_first_moves = get_winnable_first_moves(numbers)
    
    # Print the number of winnable first moves
    print(len(winnable_first_moves))

if __name__ == '__main__':
    main()

