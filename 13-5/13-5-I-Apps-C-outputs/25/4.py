
def solve(N, numbers):
    # Initialize a set to store the first moves
    first_moves = set()
    
    # Iterate through the numbers
    for i in range(N):
        # Get the current number
        current_number = numbers[i]
        
        # Check if the current number is odd
        if current_number % 2 == 1:
            # Add the current number to the set of first moves
            first_moves.add(current_number)
        
        # Check if the current number is even
        if current_number % 2 == 0:
            # Get the previous number
            previous_number = numbers[(i - 1) % N]
            
            # Check if the previous number is odd
            if previous_number % 2 == 1:
                # Add the current number to the set of first moves
                first_moves.add(current_number)
    
    # Return the length of the set of first moves
    return len(first_moves)

