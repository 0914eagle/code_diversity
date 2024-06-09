
def get_remainder(n, x, y, number):
    # Initialize the minimum number of operations to perform
    min_operations = 0
    
    # Initialize the current number
    current_number = number
    
    # Iterate over the digits of the number
    for i in range(n):
        # Check if the current digit is 0
        if current_number[i] == "0":
            # Increment the minimum number of operations
            min_operations += 1
            # Set the current digit to 1
            current_number = current_number[:i] + "1" + current_number[i+1:]
    
    # Return the minimum number of operations
    return min_operations

def main():
    # Read the input
    n, x, y = map(int, input().split())
    number = input()
    
    # Get the remainder
    remainder = get_remainder(n, x, y, number)
    
    # Print the result
    print(remainder)

if __name__ == '__main__':
    main()

