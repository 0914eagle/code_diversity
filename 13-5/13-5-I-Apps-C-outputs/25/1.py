
def solve(n, numbers):
    # Initialize a set to store the first moves
    first_moves = set()
    
    # Iterate through the numbers
    for i in range(n):
        # Get the current number
        current_number = numbers[i]
        
        # Check if the current number is odd
        if current_number % 2 == 1:
            # If the current number is odd, add it to the set of first moves
            first_moves.add(current_number)
        else:
            # If the current number is even, add its adjacent numbers to the set of first moves
            if i > 0:
                first_moves.add(numbers[i-1])
            if i < n-1:
                first_moves.add(numbers[i+1])
    
    # Return the length of the set of first moves
    return len(first_moves)

