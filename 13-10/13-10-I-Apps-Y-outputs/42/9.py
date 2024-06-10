
def get_maximum_rent(a, b, m, sigma):
    # Initialize variables
    x = 1
    y = 1
    rent = a * x + b * y

    # Loop until the constraints are satisfied
    while x + y <= m and 2 * x + y >= sigma:
        # Increase the square footage
        x += 1
        y += 1

        # Calculate the new rent
        rent = a * x + b * y

    # Return the maximum rent
    return rent

def main():
    # Read the input
    a, b = map(int, input().split())
    m, sigma = map(int, input().split())

    # Call the function and print the result
    print(get_maximum_rent(a, b, m, sigma))

if __name__ == '__main__':
    main()

