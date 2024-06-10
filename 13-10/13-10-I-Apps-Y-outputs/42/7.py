
def get_max_rent(a, b, m, sigma):
    # Function to find the maximum rent subject to the constraints
    # a: price per square foot
    # b: price per smart bulb
    # m: maximum square footage + number of smart bulbs
    # sigma: minimum number of outlets
    
    # Initialize variables
    x = 1
    y = 1
    rent = a * x + b * y
    
    # Loop until the constraints are met
    while x + y < m and 2 * x + y < sigma:
        # Increment x and y by 1 and calculate the new rent
        x += 1
        y += 1
        rent = a * x + b * y
    
    # Return the maximum rent
    return rent

def main():
    # Read the input
    a, b = map(int, input().split())
    m, sigma = map(int, input().split())
    
    # Call the function to find the maximum rent
    max_rent = get_max_rent(a, b, m, sigma)
    
    # Print the output
    print(max_rent)

if __name__ == '__main__':
    main()

