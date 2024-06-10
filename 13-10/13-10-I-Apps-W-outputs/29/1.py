
def is_consistent(n, a, b, c, d):
    # Calculate the minimum and maximum possible weight of a single grain
    min_grain_weight = a - b
    max_grain_weight = a + b
    
    # Calculate the minimum and maximum possible weight of the package
    min_package_weight = c - d
    max_package_weight = c + d
    
    # Initialize a list to store the weights of the grains
    grain_weights = []
    
    # Loop through the number of grains and calculate the weight of each grain
    for i in range(n):
        # Generate a random integer between the minimum and maximum possible weight of a single grain
        grain_weight = random.randint(min_grain_weight, max_grain_weight)
        grain_weights.append(grain_weight)
    
    # Calculate the total weight of the package
    package_weight = sum(grain_weights)
    
    # Check if the total weight of the package is within the possible range
    if min_package_weight <= package_weight <= max_package_weight:
        return True
    else:
        return False

def main():
    # Read the number of test cases
    num_test_cases = int(input())
    
    # Loop through the test cases
    for _ in range(num_test_cases):
        # Read the input
        n, a, b, c, d = map(int, input().split())
        
        # Check if the information is consistent
        if is_consistent(n, a, b, c, d):
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()

