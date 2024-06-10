
def get_min_operations(a, b):
    # Initialize the minimum number of operations to -1
    min_operations = -1
    
    # Loop through all possible divisors
    for divisor in [2, 4, 8]:
        # Check if the target value is divisible by the divisor
        if b % divisor == 0:
            # Calculate the minimum number of operations needed to reach the target value
            min_operations = min(min_operations, get_min_operations(a, b // divisor) + 1)
    
    return min_operations

def main():
    # Read the number of test cases
    num_test_cases = int(input())
    
    # Loop through each test case
    for _ in range(num_test_cases):
        # Read the initial and target values
        a, b = map(int, input().split())
        
        # Calculate the minimum number of operations needed to reach the target value
        min_operations = get_min_operations(a, b)
        
        # Print the result
        print(min_operations)

if __name__ == '__main__':
    main()

