
def get_max_rent(a, b, m, sigma):
    # Initialize variables
    x = 1
    y = 1
    R = a * x + b * y
    
    # Loop until the constraints are met
    while x + y <= m and 2 * x + y >= sigma:
        # Check if the current combination is optimal
        if a * x + b * y > R:
            R = a * x + b * y
        # Increase the square footage
        x += 1
        # Increase the number of smart bulbs
        y += 1
    
    # Return the maximum rent
    return R

def main():
    # Read input from stdin
    a, b = map(int, input().split())
    m, sigma = map(int, input().split())
    
    # Call the function and print the result
    print(get_max_rent(a, b, m, sigma))

if __name__ == '__main__':
    main()

