
def get_max_or_value(numbers, k, x):
    # Initialize the maximum OR value
    max_or_value = 0
    
    # Loop through each number
    for i in range(len(numbers)):
        # Get the current number
        current_number = numbers[i]
        
        # Loop through each operation
        for j in range(k):
            # Multiply the current number by x
            new_number = current_number * x
            
            # Check if the new number is greater than the maximum OR value
            if new_number > max_or_value:
                # Update the maximum OR value
                max_or_value = new_number
    
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

