
def get_number_of_first_moves(numbers):
    # Initialize a set to store the first moves
    first_moves = set()
    
    # Iterate over the numbers
    for i in range(len(numbers)):
        # Get the current number
        current_number = numbers[i]
        
        # Check if the current number is odd
        if current_number % 2 == 1:
            # Add the current number to the set of first moves
            first_moves.add(current_number)
        
        # Check if the current number is even
        if current_number % 2 == 0:
            # Get the previous number
            previous_number = numbers[(i - 1) % len(numbers)]
            
            # Add the previous number to the set of first moves
            first_moves.add(previous_number)
    
    # Return the length of the set of first moves
    return len(first_moves)

def main():
    # Read the number of numbers and the numbers from the input
    n = int(input())
    numbers = [int(x) for x in input().split()]
    
    # Call the get_number_of_first_moves function and print the result
    print(get_number_of_first_moves(numbers))

if __name__ == '__main__':
    main()

