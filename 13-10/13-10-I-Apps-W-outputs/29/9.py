
def check_grain_weights(n, a, b, c, d):
    
    # Initialize a list to store the weights of the n grains
    weights = []
    
    # Loop through each grain and generate a random integer weight
    for i in range(n):
        weights.append(random.randint(a - b, a + b))
    
    # Calculate the total weight of the grains
    total_weight = sum(weights)
    
    # Check if the total weight is within the given range
    if c - d <= total_weight <= c + d:
        return True
    else:
        return False

def check_package_weights(n, a, b, c, d):
    
    # Initialize a list to store the weights of the n grains
    weights = []
    
    # Loop through each grain and generate a random integer weight
    for i in range(n):
        weights.append(random.randint(a - b, a + b))
    
    # Calculate the total weight of the grains
    total_weight = sum(weights)
    
    # Check if the total weight is within the given range
    if c - d <= total_weight <= c + d:
        return True
    else:
        return False

def main():
    # Read the number of test cases
    num_cases = int(input())
    
    # Loop through each test case
    for i in range(num_cases):
        # Read the input
        n, a, b, c, d = map(int, input().split())
        
        # Check if the weights of the n grains can add up to a total weight of c - d grams
        if check_grain_weights(n, a, b, c, d):
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()

