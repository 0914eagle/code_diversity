
def get_first_moves(numbers):
    # Initialize a set to store the first moves
    first_moves = set()
    
    # Iterate over the numbers
    for i in range(len(numbers)):
        # Get the current number and its adjacent numbers
        current_number = numbers[i]
        adjacent_numbers = [numbers[(i-1)%len(numbers)], numbers[(i+1)%len(numbers)]]
        
        # Add the current number to the set of first moves if it is not already present
        if current_number not in first_moves:
            first_moves.add(current_number)
        
        # Add the adjacent numbers to the set of first moves if they are not already present
        for adjacent_number in adjacent_numbers:
            if adjacent_number not in first_moves:
                first_moves.add(adjacent_number)
    
    return len(first_moves)

def main():
    # Read the input
    N = int(input())
    numbers = [int(x) for x in input().split()]
    
    # Call the function to get the number of first moves
    result = get_first_moves(numbers)
    
    # Print the result
    print(result)

if __name__ == '__main__':
    main()

