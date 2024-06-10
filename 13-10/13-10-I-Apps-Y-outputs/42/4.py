
def get_max_rent(a, b, m, sigma):
    # Initialize variables
    x = 1
    y = 1
    rent = a + b

    # Loop until the constraints are satisfied
    while x + y <= m and 2 * x + y >= sigma:
        # Update the values of x and y
        x += 1
        y += 1

        # Update the rent
        rent = a * x + b * y

    # Return the maximum rent
    return rent

def main():
    # Read the input
    a, b = map(int, input().split())
    m, sigma = map(int, input().split())

    # Call the function to get the maximum rent
    max_rent = get_max_rent(a, b, m, sigma)

    # Print the output
    print(max_rent)

if __name__ == '__main__':
    main()

