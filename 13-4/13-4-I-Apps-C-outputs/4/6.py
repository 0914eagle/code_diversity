
def get_max_or(numbers, k, x):
    # Sort the numbers in descending order
    numbers.sort(reverse=True)
    
    # Initialize the maximum OR value
    max_or = 0
    
    # Loop through the numbers and perform the operations
    for i in range(k):
        # Multiply the current number by x
        numbers[i] *= x
        
        # Update the maximum OR value
        max_or = max(max_or, numbers[i] | numbers[i+1])
    
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

