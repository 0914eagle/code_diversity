
def get_shuffling_operations(n, s, t, shuffling_operations):
    # Initialize a list to store the positions of the glasses
    glasses = list(range(1, n+1))
    
    # Initialize a variable to store the number of shuffling operations
    num_operations = 0
    
    # Loop through the shuffling operations
    for operation in shuffling_operations:
        # Get the current position of the marble
        current_position = glasses.index(s)
        
        # Perform the shuffling operation
        glasses = perform_shuffling_operation(glasses, operation)
        
        # Increment the number of shuffling operations
        num_operations += 1
        
        # Check if the marble has reached the final position
        if glasses.index(s) == t:
            break
    
    # Return the number of shuffling operations needed to get the marble to the final position
    return num_operations

def perform_shuffling_operation(glasses, operation):
    # Split the operation into two parts
    a, b = operation
    
    # Get the current position of the first glass
    current_position = glasses.index(a)
    
    # Move the first glass to the new position
    glasses[current_position] = b
    
    # Return the updated list of glasses
    return glasses

def main():
    # Read the input
    n, s, t = map(int, input().split())
    shuffling_operations = list(map(int, input().split()))
    
    # Get the number of shuffling operations needed to get the marble to the final position
    num_operations = get_shuffling_operations(n, s, t, shuffling_operations)
    
    # Print the number of shuffling operations
    print(num_operations)

if __name__ == '__main__':
    main()

