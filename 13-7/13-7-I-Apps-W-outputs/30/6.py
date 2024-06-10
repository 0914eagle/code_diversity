
def get_min_operations(a, b):
    if a == b:
        return 0
    
    # Initialize the minimum number of operations to infinity
    min_operations = float('inf')
    
    # Iterate over the possible operations
    for operation in [2, 4, 8]:
        # Check if the current operation is possible
        if a % operation == 0:
            # Calculate the new value after the operation
            new_value = a // operation
            
            # Check if the new value is the target value
            if new_value == b:
                # If it is, return the current minimum number of operations
                return min_operations
            else:
                # If it's not, calculate the minimum number of operations for the new value
                min_operations = min(min_operations, 1 + get_min_operations(new_value, b))
    
    # If no operation is possible, return -1
    return -1

def main():
    # Read the number of test cases
    t = int(input())
    
    # Iterate over the test cases
    for _ in range(t):
        # Read the initial and target values
        a, b = map(int, input().split())
        
        # Calculate the minimum number of operations
        min_operations = get_min_operations(a, b)
        
        # Print the result
        print(min_operations)

if __name__ == '__main__':
    main()

