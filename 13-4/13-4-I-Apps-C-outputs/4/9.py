
def get_max_or(numbers, k, x):
    # Initialize the maximum OR value
    max_or = 0
    
    # Loop through each number
    for i in range(len(numbers)):
        # Get the current number
        num = numbers[i]
        
        # Loop through each operation
        for j in range(k):
            # Multiply the number by x
            num *= x
            
            # Update the maximum OR value
            max_or = max(max_or, num)
    
    # Return the maximum OR value
    return max_or

def main():
    # Read the input
    n, k, x = map(int, input().split())
    numbers = list(map(int, input().split()))
    
    # Get the maximum OR value
    max_or = get_max_or(numbers, k, x)
    
    # Print the result
    print(max_or)

if __name__ == '__main__':
    main()

