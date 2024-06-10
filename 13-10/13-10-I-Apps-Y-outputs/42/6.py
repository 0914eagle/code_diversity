
def find_max_rent(a, b, m, sigma):
    # Initialize the maximum rent as 0
    max_rent = 0
    
    # Loop through all possible values of x and y that satisfy the constraints
    for x in range(1, m + 1):
        for y in range(1, m + 1):
            # Calculate the current rent
            current_rent = a * x + b * y
            
            # Check if the current rent is greater than the maximum rent
            if current_rent > max_rent:
                # Update the maximum rent if necessary
                max_rent = current_rent
    
    # Return the maximum rent
    return max_rent

def main():
    # Read the input
    a, b, m, sigma = map(int, input().split())
    
    # Find the maximum rent
    max_rent = find_max_rent(a, b, m, sigma)
    
    # Print the maximum rent
    print(max_rent)

if __name__ == '__main__':
    main()

