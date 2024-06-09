
def get_max_or_value(numbers, k, x):
    # Sort the numbers in descending order
    numbers.sort(reverse=True)
    
    # Initialize the maximum OR value
    max_or_value = 0
    
    # Loop through the numbers
    for i in range(len(numbers)):
        # Check if we can perform an operation
        if k > 0:
            # Multiply the current number by x
            numbers[i] *= x
            
            # Decrement the number of operations
            k -= 1
            
            # Update the maximum OR value
            max_or_value = max(max_or_value, numbers[i])
    
    # Return the maximum OR value
    return max_or_value

def main():
    # Read the input
    n, k, x = map(int, input().split())
    numbers = list(map(int, input().split()))
    
    # Get the maximum OR value
    max_or_value = get_max_or_value(numbers, k, x)
    
    # Print the result
    print(max_or_value)

if __name__ == '__main__':
    main()

